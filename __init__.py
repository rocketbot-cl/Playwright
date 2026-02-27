# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"

    pip install <package> -t .

"""
# -*- coding: utf-8 -*-
__version__ = '1.0.0'
__author__ = 'Rocketbot <contacto@rocketbot.com>'
global cur_path
base_path = tmp_global_obj["basepath"]
cur_path = base_path + 'modules' + os.sep + 'playwright' + os.sep + 'libs' + os.sep

if cur_path not in sys.path:
    sys.path.append(cur_path)

global _ensure_playwright_browsers_installed, glob, playwright_cli

from PlaywrightObject import PlaywrightObject
from playwright.__main__ import main as playwright_cli
import os
import subprocess
import sys

import glob

# Global singleton (module lifetime)
# In Rocketbot, this file is imported per execution context;
# if your engine reloads modules, you may need a more persistent store.
global _PW
try:
    _PW
except NameError:
    _PW = PlaywrightObject()
    
GetGlobals = GetGlobals #pylint: disable=undefined-variable,self-assigning-variable
GetParams = GetParams #pylint: disable=undefined-variable,self-assigning-variable
SetVar = SetVar #pylint: disable=undefined-variable,self-assigning-variable
PrintException = PrintException #pylint: disable=undefined-variable,self-assigning-variable
tmp_global_obj = tmp_global_obj #pylint: disable=undefined-variable,self-assigning-variable

module = GetParams("module")

# --------------------------
# Utils
# --------------------------
def _to_bool(v):
    if isinstance(v, bool):
        return v
    if v is None:
        return False
    return str(v).strip().lower() in ("1", "true", "yes", "y", "si")


import os
import sys
import time
from time import sleep


def _ensure_playwright_browsers_installed(base_path, browser_type="chromium"):
    import time
    from time import sleep

    target_path = os.path.join(
        base_path, "playwright", "driver", "package", ".local-browsers"
    ) + os.sep

    os.makedirs(target_path, exist_ok=True)

    bt = (browser_type or "chromium").lower().strip()
    if bt not in ("chromium", "webkit"): 
        raise Exception("browser_type must be chromium|webkit")

    if bt == "chromium":
        exe_ok = bool(glob.glob(os.path.join(target_path, "chromium-*", "chrome-win", "chrome.exe"))) or \
                 bool(glob.glob(os.path.join(target_path, "chromium-*", "chrome-win64", "chrome.exe")))
    #elif bt == "firefox":
    #    exe_ok = bool(glob.glob(os.path.join(target_path, "firefox-*", "firefox", "firefox.exe")))
    else:  # webkit
        exe_ok = bool(glob.glob(os.path.join(target_path, "webkit-*", "**", "*.exe"), recursive=True))

    if exe_ok:
        os.environ["PLAYWRIGHT_BROWSERS_PATH"] = target_path
        return

    # --- lock to avoid parallel install race ---
    lock_file = os.path.join(target_path, ".install.lock")
    start = time.time()
    while True:
        try:
            fd = os.open(lock_file, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
            os.close(fd)
            break
        except FileExistsError:
            if time.time() - start > 180:
                raise Exception("Timeout waiting for Playwright browsers installation lock.")
            sleep(1)

    try:
        # re-check after lock
        if bt == "chromium":
            exe_ok = bool(glob.glob(os.path.join(target_path, "chromium-*", "chrome-win", "chrome.exe"))) or \
                     bool(glob.glob(os.path.join(target_path, "chromium-*", "chrome-win64", "chrome.exe")))
        #elif bt == "firefox":
        #    exe_ok = bool(glob.glob(os.path.join(target_path, "firefox-*", "firefox", "firefox.exe")))
        else:
            exe_ok = bool(glob.glob(os.path.join(target_path, "webkit-*", "**", "*.exe"), recursive=True))

        if exe_ok:
            os.environ["PLAYWRIGHT_BROWSERS_PATH"] = target_path
            return

        os.environ["PLAYWRIGHT_BROWSERS_PATH"] = target_path

        original_argv = sys.argv
        try:
            # instala SOLO el browser seleccionado
            sys.argv = ["playwright", "install", bt]
            playwright_cli()
        except SystemExit as exit:
            if exit.code != 0:
                raise Exception(f"Playwright install failed with exit code: {exit.code}")
        finally:
            sys.argv = original_argv

        # validate again
        if bt == "chromium":
            exe_ok = bool(glob.glob(os.path.join(target_path, "chromium-*", "chrome-win", "chrome.exe"))) or \
                     bool(glob.glob(os.path.join(target_path, "chromium-*", "chrome-win64", "chrome.exe")))
        #elif bt == "firefox":
        #    exe_ok = bool(glob.glob(os.path.join(target_path, "firefox-*", "firefox", "firefox.exe")))
        else:
            exe_ok = bool(glob.glob(os.path.join(target_path, "webkit-*", "**", "*.exe"), recursive=True))

        if not exe_ok:
            raise Exception("Playwright install finished but browser executable was not found in .local-browsers. Check internet/proxy restrictions.")

    finally:
        try:
            os.remove(lock_file)
        except Exception:
            pass

# --------------------------
# Commands
# --------------------------
if module == "stop_playwright":
    session_id = GetParams("session_id")
    _PW.stop(session_id)
    res = GetParams("result")
    if res:
        SetVar(res, True)

if module == "goto":
    session_id = GetParams("session_id")
    url = GetParams("url")
    wait_until = (GetParams("wait_until") or "load").strip().lower()
    timeout = int(GetParams("timeout_sec") or 30)
    open_in_new_tab = _to_bool(GetParams("open_in_new_tab"))

    timeout *= 1000

    if open_in_new_tab:
        _PW.new_page(session_id)

    res = GetParams("result")
    
    try:
        _PW.goto(session_id=session_id, url=url, wait_until=wait_until, timeout=timeout )
        if res:
            SetVar(res, True)

    except Exception as e:
        if res:
            SetVar(res, False)
        raise e


if module == "open_browser":
    session_id = GetParams("session_id")
    browser_type = GetParams("browser_type") or "chromium"
    headless = _to_bool(GetParams("headless"))
    executable_path = GetParams("executable_path")
    profile_path = GetParams("profile_path") or ""

    proxy_server = GetParams("proxy_server") or ""
    proxy_user = GetParams("proxy_user") or ""
    proxy_pass = GetParams("proxy_pass") or ""

    url = GetParams("url") or ""
    timeout = int(GetParams("timeout_sec") or 30)

    timeout *= 1000

    try:
        if browser_type == "chromium" and not executable_path:
            raise Exception("Browser executable path is required")
        
        elif executable_path and not os.path.exists(executable_path):
            raise Exception("The specified executable path does not exist")

        _ensure_playwright_browsers_installed(cur_path, browser_type)
        _PW.start(session_id, base_path)


        _PW.launch_browser(
            session_id = session_id,
            browser_type = browser_type,
            headless = headless,
            proxy_server = proxy_server,
            proxy_user = proxy_user,
            proxy_pass = proxy_pass,
            executable_path = executable_path,
            profile_path = profile_path
        )

        if url:
            _PW.goto(session_id=session_id, url=url, wait_until="load", timeout=timeout)


    except Exception as e:
        try:
            PrintException()
        except Exception:
            print(str(e).encode("utf-8", "replace").decode("utf-8", "replace"))

        raise e

if module == "wait_for_selector":
    session_id = GetParams("session_id")
    selector = GetParams("selector")
    selector_type = GetParams("selector_type") or "css"
    state = (GetParams("state") or "visible").strip().lower()
    timeout = int(GetParams("timeout_sec") or 30)
    res = GetParams("result")

    timeout *= 1000

    loc = _PW.locator(session_id, selector, selector_type)
    try:
        loc.wait_for(state=state, timeout=timeout)
        if res:
            SetVar(res, True)
    except:
        if res:
            SetVar(res, False)

if module == "click":
    session_id = GetParams("session_id")
    selector = GetParams("selector")
    selector_type = GetParams("selector_type") or "css"
    timeout = int(GetParams("timeout_sec") or 30)
    force = _to_bool(GetParams("force"))

    timeout *= 1000

    loc = _PW.locator(session_id, selector, selector_type)
    loc.click(timeout=timeout, force=force)

if module == "send_Text":
    session_id = GetParams("session_id")
    selector = GetParams("selector")
    selector_type = GetParams("selector_type") or "css"
    text = GetParams("text") or ""
    special_key = GetParams("special")
    timeout = int(GetParams("timeout_sec") or 30)

    timeout *= 1000

    loc = _PW.locator(session_id, selector, selector_type)
    loc.fill(text, timeout=timeout)
    if special_key:
        loc.press(special_key, timeout=timeout)

if module == "extract_text":
    session_id = GetParams("session_id")
    selector = GetParams("selector")
    selector_type = GetParams("selector_type") or "css"
    timeout = int(GetParams("timeout_sec") or 30)

    timeout *= 1000

    loc = _PW.locator(session_id, selector, selector_type)
    value = loc.inner_text(timeout=timeout)

    SetVar(GetParams("result"), value)

if module == "screenshot":
    session_id = GetParams("session_id")
    path = GetParams("folder_path")
    file_name = GetParams("file_name")
    full_page = _to_bool(GetParams("full_page"))

    if path is None:
        raise Exception("Folder path cannot be left Empty")
    if file_name is None:
        file_name = "screenshot"

    _PW.screenshot(session_id, path, file_name, full_page)


if module == "expect_download_click":
    """
    Clicks an element and waits for download, then saves it.
    """
    session_id = GetParams("session_id")
    selector = GetParams("selector")
    selector_type = GetParams("selector_type") or "css"
    save_dir = GetParams("save_dir") or ""
    file_name = GetParams("file_name") or ""   # optional override
    timeout = int(GetParams("timeout_sec") or 60)

    timeout *= 1000

    file_path, file_name = _PW.download(session_id=session_id, selector= selector, save_dir=save_dir, file_name=file_name, timeout=timeout, selector_type=selector_type)

    out_path_var = GetParams("out_path")
    out_name_var = GetParams("out_filename")

    if out_path_var:
        SetVar(out_path_var, file_path)
    if out_name_var:
        SetVar(out_name_var, file_name)

if module == "select_option":
    session_id = GetParams("session_id")
    selector = GetParams("selector")
    selector_type = GetParams("selector_type") or "css"
    options = GetParams("options")
    select_by = GetParams("select_by"),
    timeout = int(GetParams("timeout_sec") or 30)

    timeout *= 1000

    loc = _PW.locator(session_id, selector, selector_type)

    options = options.strip("[]").split(", ")

    if select_by[0] == "Index": 
        indexes = [int(option) for option in options]
        loc.select_option(index=indexes, timeout=timeout)
    
    elif select_by[0] == "Label":
        loc.select_option(label=options, timeout=timeout)
    
    else:
        loc.select_option(value=options, timeout=timeout)

if module == "sendKeyCombination":
    key = GetParams("key")
    first_special = GetParams("first_special_key")
    second_special = GetParams("second_special_key")
    session_id = GetParams("session_id")
    
    ctx = _PW.page(session_id)
    combination = []

    if first_special:
        combination.append(first_special)

    if second_special:
        combination.append(second_special)

    if key:
        combination.append(key)
    
    final_combination = "+".join(combination)
    ctx.keyboard.press(final_combination)

if module == "set_checked":
    session_id = GetParams("session_id")
    selector = GetParams("selector")
    selector_type = GetParams("selector_type") or "css"
    timeout = int(GetParams("timeout_sec") or 30)
    check = GetParams("check")

    timeout *= 1000

    loc = _PW.locator(session_id, selector, selector_type)
    loc.set_checked(check, timeout=timeout)

if module == "get_attribute":
    session_id = GetParams("session_id")
    selector = GetParams("selector")
    selector_type = GetParams("selector_type") or "css"
    timeout = int(GetParams("timeout_sec") or 30)
    attribute = GetParams("attribute")
    res = GetParams("result")

    timeout *= 1000

    loc = _PW.locator(session_id, selector, selector_type)
    value = loc.get_attribute(attribute, timeout=timeout)

    SetVar(res, value)

if module == "wait_for_load_state":
    session_id = GetParams("session_id")
    timeout = int(GetParams("timeout_sec") or 30)
    load_state = GetParams("load_state")
    res = GetParams("result")

    timeout *= 1000

    ctx = _PW.content(session_id)
    if load_state is None:
        load_state = "load"
    try:
        ctx.wait_for_load_state(state=load_state, timeout=timeout)
        SetVar(res, True)
    except:
        SetVar(res, False)
    
if module == "switch_tab":
    session_id = GetParams("session_id")
    page_title = GetParams("title")

    _PW.change_page_by_title(session_id=session_id, page_title=page_title)

if module == "get_tab_titles":
    session_id = GetParams("session_id")
    res = GetParams("result")

    titles = _PW.page_titles(session_id)
    SetVar(res, titles)

if module == "evaluate_js":
    session_id = GetParams("session_id")
    js_code = GetParams("js_code")
    res = GetParams("result")
    parameters = GetParams("function_parameters")

    ctx = _PW.content(session_id)
    if parameters:
        list_param = [item for item in parameters.strip("[]").split(", ")]
        return_value = ctx.evaluate(js_code, list_param)
    else:
        return_value = ctx.evaluate(js_code)
        
    SetVar(res, return_value)

if module == "count":
    session_id = GetParams("session_id")
    selector = GetParams("selector")
    selector_type = GetParams("selector_type") or "css"
    res = GetParams("result")

    loc = _PW.locator(session_id, selector, selector_type)
    count = loc.count()
    if count == 0:
        SetVar(res, "There were no elements found")
    else:
        SetVar(res, count)
        
if module == "change_to_Iframe":
    session_id = GetParams("session_id")
    selector = GetParams("selector")
    selector_type = GetParams("selector_type") or "css"

    _PW.switch_to_iframe(session_id, selector, selector_type)

if module == "change_to_body_content":
    session_id = GetParams("session_id")

    _PW.change_to_body_content(session_id)