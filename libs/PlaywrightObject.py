# -*- coding: utf-8 -*-
import os
from typing import Dict, Any, Optional

from playwright.sync_api import sync_playwright, Playwright, Browser, BrowserContext, Page, FrameLocator


class PlaywrightObject:
    """
    Session manager: each session_id holds playwright + browser + context + page
    to allow parallel executions safely.
    """

    def __init__(self):
        self.sessions: Dict[str, Dict[str, Any]] = {}
        self._pw: Optional[Playwright] = None
        self._pw_refcount: int = 0

    def _get(self, session_id: str) -> Dict[str, Any]:
        if session_id not in self.sessions:
            raise Exception(f"Session '{session_id}' not found. Run start_playwright first.")
        return self.sessions[session_id]

    def start(self, session_id: str) -> None:

        if session_id in self.sessions:
            return

        if self._pw is None:
            self._pw = sync_playwright().start()

        self._pw_refcount += 1
        self.sessions[session_id] = {
            "playwright": self._pw,
            "browser": None,
            "context": None,
            "page": None,
            "iframe": None
        }

    def stop(self, session_id: str) -> None:
        s = self._get(session_id)
        # close page/context/browser in safe order
        try:
            if s.get("page"):
                s["page"].close()
        except:
            pass
        try:
            ctx = s.get("context")
            if ctx:
                profile_file = s.get("storage_state_path")
                if profile_file:
                    ctx.storage_state(path=profile_file)
                    
                ctx.close()
        except:
            pass
        try:
            if s.get("browser"):
                s["browser"].close()
        except:
            pass

        self.sessions.pop(session_id, None)

        self._pw_refcount = max(0, self._pw_refcount - 1)
        if self._pw_refcount == 0 and self._pw is not None:
            try:
                self._pw.stop()
            finally:
                self._pw = None
    
    def launch_browser(self, session_id: str, browser_type: str = "chromium", headless: bool = True,
                      proxy_server: str = "", proxy_user: str = "", proxy_pass: str = "",
                      downloads_path: str = "") -> None:
        
        s = self._get(session_id)
        pw: Playwright = s["playwright"]

        bt = browser_type.lower().strip()
        if bt not in ("chromium", "firefox", "webkit"):
            raise Exception("browser_type must be chromium|firefox|webkit")

        proxy = None
        if proxy_server:
            proxy = {"server": proxy_server}
            if proxy_user:
                proxy["username"] = proxy_user
            if proxy_pass:
                proxy["password"] = proxy_pass


        ignore_default_args = ["--enable-automation"]
        browser_launcher = getattr(pw, bt)

        if bt == "chromium":
            args = [
                "--disable-blink-features=AutomationControlled",
                "--start-maximized",
                f"--download-default-directory={downloads_path}"
            ]
            s["browser"] = browser_launcher.launch(headless=headless, proxy=proxy, args=args, ignore_default_args=ignore_default_args)

        elif bt == "firefox":
            s["browser"] = browser_launcher.launch(headless=headless, proxy=proxy, ignore_default_args=ignore_default_args)
            
        # store downloads_path for context creation
        if downloads_path:
            s["downloads_path"] = downloads_path

    def new_context(self, session_id: str,
                    viewport_w: int = 1366, viewport_h: int = 768,
                    user_agent: str = "", locale: str = "",
                    storage_state_path: str = "") -> None:
        s = self._get(session_id)
        browser: Browser = s.get("browser")
        if not browser:
            raise Exception("Browser not launched. Run launch_browser first.")

        kwargs = {
            "accept_downloads": True,
            "no_viewport": True,
        }

        if user_agent:
            kwargs["user_agent"] = user_agent
        if locale:
            kwargs["locale"] = locale

        # IMPORTANT: storage_state can be loaded to reuse login
        if storage_state_path:
            kwargs["storage_state"] = storage_state_path
            
        s["storage_state_path"] = storage_state_path

        # downloads_path is supported in new_context in newer versions;
        # but to be safe, we handle downloads by download.save_as(...)
        # We'll still store it for our own default save path.
        s["context"] = browser.new_context(**kwargs)


    def new_page(self, session_id: str) -> None:
        s = self._get(session_id)
        ctx: BrowserContext = s.get("context")
        if not ctx:
            raise Exception("Context not created. Run new_context first.")
        s["page"] = ctx.new_page()
        s["iframe"] = None

    def page(self, session_id: str) -> Page:
        s = self._get(session_id)
        p: Page = s.get("page")
        if not p:
            raise Exception("Page not available. Run new_page first.")
        return p

    def content(self, session_id: str):
        s = self._get(session_id)
        f: FrameLocator = s.get("iframe")
        if f:
            return f
        
        p: Page = s.get("page")
        if not p:
            raise Exception("Page not available. Run new_page first.")
        return p
    

    def goto(self, session_id: str, url: str, wait_until: str, timeout:int):
        self.change_to_body_content(session_id)
        page = self.content(session_id)
        page.goto(url, wait_until=wait_until, timeout=timeout)


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


    def change_page_by_title(self, session_id: str, page_title: str) -> None:
        s = self._get(session_id)
        ctx: BrowserContext = s.get("context")

        if not ctx:
            raise Exception("Context not created. Run new_context first.")
        
        pages = ctx.pages
        for page in pages:
            if page.title() == page_title:
                s["page"] = page
                s["iframe"] = None
                page.bring_to_front()
                break
        raise Exception("The page could not be found.")


    # --- selector helpers ---
    def locator(self, session_id: str, selector: str, selector_type: str = "css"):
        c = self.content(session_id)

        st = (selector_type or "css").lower().strip()
        if st == "css":
            return c.locator(selector)
        if st == "xpath":
            return c.locator(f"xpath={selector}")
        if st == "text":
            return c.locator(f"text={selector}")
        # simple fallback
        return c.locator(selector)
    

    def switch_to_iframe(self, session_id: str, selector: str, selector_type: str = "css"):
        s = self._get(session_id)
        c = self.content(session_id)

        st = (selector_type or "css").lower().strip()
        if st == "css":
            iframe = c.frame_locator(selector)
        elif st == "xpath":
            iframe = c.frame_locator(f"xpath={selector}")
        elif st == "text":
            iframe = c.frame_locator(f"text={selector}")
        else:
            iframe = c.frame_locator(selector)

        s["iframe"] = iframe
    

    def change_to_body_content(self, session_id: str):
        s = self._get(session_id)
        s["iframe"] = None

    def download(self, session_id: str, selector: str, save_dir: str, file_name: str, timeout: int, selector_type: str = "css"):
        s = self._get(session_id)

        if not save_dir:
            try:
                save_dir = s["downloads_path"]
            except:
                raise Exception("Save Directory cannot be left empty")
    
        p = self.page(session_id)
        loc = self.locator(session_id, selector, selector_type)

        with p.expect_download(timeout=timeout) as dl_info:
            loc.click()

        dl = dl_info.value
        suggested = dl.suggested_filename

        if not file_name:
            file_name = suggested
        else:
            #We add to the file name the suggested Filename extension
            suggested = suggested.split(".")
            file_name += "." + suggested[1]

        os.makedirs(save_dir, exist_ok=True)
        final_path = os.path.join(save_dir, file_name)
        dl.save_as(final_path)

        return final_path, file_name