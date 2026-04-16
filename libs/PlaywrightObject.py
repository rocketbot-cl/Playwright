# -*- coding: utf-8 -*-
import os
import shutil
import tempfile
import stat
from typing import Dict, Any, Optional

from playwright.sync_api import (
    sync_playwright,
    Playwright,
    Browser,
    BrowserContext,
    Page,
    Frame,
)


class PlaywrightObject:
    """
    Session manager:
    - Single Playwright instance per process
    - Multiple parallel browser sessions
    - Proper iframe handling using real Frame objects
    """

    def __init__(self):
        self.sessions: Dict[str, Dict[str, Any]] = {}
        self._pw: Optional[Playwright] = None
        self._pw_refcount: int = 0

    def _get(self, session_id: str) -> Dict[str, Any]:
        if session_id not in self.sessions:
            raise Exception(f"Session '{session_id}' not found.")
        return self.sessions[session_id]

    def start(self, session_id: str, base_path: str) -> None:
        if session_id in self.sessions:
            self.__clean_temp_profile__(session_id)
            return

        if self._pw is None:
            self._pw = sync_playwright().start()

        self._pw_refcount += 1


        self.sessions[session_id] = {
            "context": None,
            "page": None,
            "current_context": None,  # Page or Frame
            "profile_path": None,
            "downloads_path": None,
        }

    def stop(self, session_id: str) -> None:
        s = self._get(session_id)

        try:
            if s.get("page"):
                s["page"].close()
        except:
            pass

        try:
            if s.get("context"):
                s["context"].close()
                s["context"] = None
        except:
            pass


        self.__clean_temp_profile__(session_id)

        self.sessions.pop(session_id, None)

        self._pw_refcount = max(0, self._pw_refcount - 1)
        if self._pw_refcount == 0 and self._pw is not None:
            try:
                self._pw.stop()
            finally:
                self._pw = None

    def launch_chrome(self,
        session_id: str,
        headless: bool = True,
        proxy_server: str = "",
        proxy_user: str = "",
        proxy_pass: str = "",
        executable_path: str = "",
        profile_path: str = "",
        debugging_port: str = "") -> None:

        s = self._get(session_id)
        pw: Playwright = self._pw

        proxy = None
        if proxy_server:
            proxy = {"server": proxy_server}
            if proxy_user:
                proxy["username"] = proxy_user
            if proxy_pass:
                proxy["password"] = proxy_pass

        browser_launcher = getattr(pw, "chromium")

        ignore_default_args = [
            "--enable-automation",
        ]

        if not profile_path.strip():
            prefix = f"rocketbot_playwrightsession_{session_id}_"
            profile_path = tempfile.mkdtemp(prefix=prefix)

        ignore_default_args.append("--disable-extensions")

        args = [
            "--disable-blink-features=AutomationControlled",
            "--start-maximized"
        ]
        
        if debugging_port:
            args.append(f"--remote-debugging-port={debugging_port}")

        browser = browser_launcher.launch_persistent_context(
            user_data_dir= profile_path,
            headless=headless,
            proxy=proxy,
            args=args,
            ignore_default_args=ignore_default_args,
            no_viewport = True,
            accept_downloads = True,
            executable_path = executable_path
        )

        s["context"] = browser
        self.new_page(session_id)
        if len(browser.pages) > 1:
            browser.pages[0].close()

    def new_page(self, session_id: str) -> None:
        s = self._get(session_id)
        ctx: BrowserContext = s.get("context")
        if not ctx:
            raise Exception("Context not created.")

        page = ctx.new_page()
        s["page"] = page
        s["current_context"] = page  # default context is page

    def page(self, session_id: str) -> Page:
        s = self._get(session_id)
        return s["page"]

    def content(self, session_id: str):
        """
        Returns current active context:
        - Page if not inside iframe
        - Frame if switched into iframe
        """
        s = self._get(session_id)
        ctx = s.get("current_context")
        if ctx:
            return ctx
        raise Exception("No active context.")

    def goto(self, session_id: str, url: str, wait_until: str, timeout: int):
        self.change_to_body_content(session_id)
        ctx = self.content(session_id)
        ctx.goto(url, wait_until=wait_until, timeout=timeout)

    def switch_to_iframe(
        self, session_id: str, selector: str, selector_type: str = "css"
    ):
        s = self._get(session_id)
        content = self.content(session_id)

        st = (selector_type or "css").lower().strip()

        if st == "css":
            frame_element = content.locator(selector).first
        elif st == "xpath":
            frame_element = content.locator(f"xpath={selector}").first
        elif st =="text":
            frame_element = content.locator(f"text={selector}").first
        else: #st == 'id'
            frame_element = content.locator(f"id={selector}").first

        handle = frame_element.element_handle(timeout=5000)
        if handle is None:
            raise Exception("Iframe element not found.")

        frame = handle.content_frame()
        if frame is None:
            raise Exception("Could not resolve iframe content.")

        s["current_context"] = frame

    def change_to_body_content(self, session_id: str):
        s = self._get(session_id)
        s["current_context"] = s["page"]

    def locator(
        self, session_id: str, selector: str, selector_type: str = "css"
    ):
        ctx = self.content(session_id)

        st = (selector_type or "css").lower().strip()

        if st == "css":
            return ctx.locator(selector)
        elif st == "xpath":
            return ctx.locator(f"xpath={selector}")
        elif st == "text":
            return ctx.locator(f"text={selector}")
        else: #st == 'id'
            return ctx.locator(f"id={selector}")

    def download(
        self,
        session_id: str,
        selector: str,
        save_dir: str,
        file_name: str,
        timeout: int,
        selector_type: str = "css",
    ):

        s = self._get(session_id)

        if not save_dir:
            save_dir = s.get("downloads_path")
            if not save_dir:
                raise Exception("Save directory cannot be empty.")

        page = s["page"]
        loc = self.locator(session_id, selector, selector_type)

        with page.expect_download(timeout=timeout) as dl_info:
            loc.click()

        dl = dl_info.value
        suggested = dl.suggested_filename

        if not file_name:
            file_name = suggested
        else:
            ext = suggested.split(".")[-1]
            file_name = f"{file_name}.{ext}"

        os.makedirs(save_dir, exist_ok=True)
        final_path = os.path.join(save_dir, file_name)
        dl.save_as(final_path)

        return final_path, file_name
    
    def screenshot(self, session_id, path, file_name, full_page):
        content = self.content(session_id)

        file_name += ".jpg"
        full_path = os.path.join(path, file_name)

        if isinstance(content, Page):
            content.screenshot(path=full_path, full_page=full_page )
        else:
            handle = content.frame_element()
            handle.screenshot(path=full_path)

    def page_titles(self, session_id: str) -> list[str]:
        s = self._get(session_id)
        ctx: BrowserContext = s.get("context")

        if not ctx:
            raise Exception("Context not created. Run new_context first.")
        
        titles = []
        pages = ctx.pages
        for page in pages:
            titles.append(page.title())
        return titles

    def change_page(self, session_id: str, page_title: str ="", index: str = "") -> None:
        s = self._get(session_id)
        ctx: BrowserContext = s.get("context")

        if not ctx:
            raise Exception("Context not created. Run new_context first.")
        
        pages = ctx.pages

        if index:
            try:
                target_page = pages[int(index)]
            except Exception as e:
                raise e
            
        else:
            for page in pages:
                if page.title() == page_title:
                    target_page = page
                    break

        if target_page:    
            s["page"] = target_page
            s["current_context"] = target_page
            s["iframe"] = None
            target_page.bring_to_front()
            
        else:
            raise Exception("The page could not be found.")

    def click_and_switch_to_tab(self, session_id: str, state: str, timeout: int, selector: str, selector_type: str = "css"):
        s = self._get(session_id)
        page = self.page(session_id)
        loc = self.locator(session_id, selector, selector_type)

        with page.expect_popup(timeout=timeout) as page_info:
            loc.click()

        new_page = page_info.value
        new_page.bring_to_front()
        new_page.wait_for_load_state(state=state)
        s["page"] = new_page
        s["current_context"] = new_page

    def upload_file(self, session_id: str, timeout: int, selector: str, path: str, selector_type: str = "css"):
        s = self._get(session_id)

        page = self.page(session_id)
        loc = self.locator(session_id, selector, selector_type)

        with page.expect_file_chooser(timeout=timeout) as fc_info:
            loc.click()

        file_chooser = fc_info.value
        file_chooser.set_files(path, timeout=timeout)

    def click_and_handle_popup(self, session_id: str, timeout: int, selector: str, interaction: str = "", selector_type: str = "css"):
        page = self.page(session_id=session_id)
        loc = self.locator(session_id, selector, selector_type)

        def handle_dialog(dialog):
            if interaction == "Accept":
                dialog.accept()
            else:
                dialog.dismiss()

        page.once("dialog", handle_dialog)

        try:
            loc.click(timeout=timeout)

        except Exception as e:
            page.remove_listener("dialog", handle_dialog)
            raise e
        
    def close_tab(self, session_id: str, page_title: str ="", index: str = ""):
        s = self._get(session_id)
        ctx: BrowserContext = s.get("context")

        if not ctx:
            raise Exception("Context not created. Run new_context first.")
        
        pages = ctx.pages

        if index:
            try:
                target_page = pages[int(index)]
            except Exception as e:
                raise e
        
        else:
            for page in pages:
                if page.title() == page_title:
                    target_page = page
                    break
        
        if target_page:
            try:
                target_page.close()
            except Exception as e:
                raise Exception(f"Tab could not be clossed. Error: {e}")
        else:
            raise Exception("The page could not be found.")


    def __clean_temp_profile__(self, session_id):
        temp_profile_dir = tempfile.gettempdir()
        prefix = f"rocketbot_playwrightsession_{session_id}_"

        for item in os.listdir(temp_profile_dir):
            if item.startswith(prefix):
                profile_path = os.path.join(temp_profile_dir, item)

                try:
                    shutil.rmtree(profile_path, onerror=self.__remove_readonly_files__)
                except Exception as e:
                    raise Exception(f"There is already an active browser using this session. Please close the browser or use another session")

    def __remove_readonly_files__(self, func, path, excinfo):
        if not os.access(path, os.W_OK):
            os.chmod(path, stat.S_IWRITE)
            func(path)
        else:
            raise