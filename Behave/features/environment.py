import sys,os,time
from playwright.sync_api import sync_playwright

# Add the Behave directory to Python path so step files can import pages, locators, utilities
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

def before_all(context):
    """Set up Playwright before all tests."""
    context.playwright = sync_playwright().start()
    context.browser_context = context.playwright.webkit.launch(
        headless=False,
        slow_mo=1000,
        args=["--start-maximized"]
    )
    
# def before_all(context):
#     time.sleep(3)
#     """Launch browser based on -D browser=<name> (chrome|firefox|webkit)."""
#     browser_name = context.config.userdata.get("browser", "chromium").lower()  # Default chromium
#     context.playwright = sync_playwright().start()

#     launch_options = {
#         "headless": False,
#         "slow_mo": 1000,
#     }

#     if browser_name == "chromium" or browser_name == "chrome":
#         launch_options["args"] = ["--start-maximized"]
#         context.browser = context.playwright.chromium.launch(**launch_options)
#     elif browser_name == "firefox":
#         context.browser = context.playwright.firefox.launch(**launch_options)
#     elif browser_name == "webkit":
#         context.browser = context.playwright.webkit.launch(**launch_options)
#     else:
#         raise ValueError(f"Unsupported browser: {browser_name}. Use: chrome, firefox, webkit")

#     # New context: NO viewport for true maximize (fixes restore-down issue)
#     context.browser_context = context.browser.new_context(no_viewport=True)  # Key fix!
#     context.page = context.browser_context.new_page()
#     context.page.set_viewport_size({"width": 1920, "height": 1080})  # Fallback for Firefox/WebKit
    
    
def before_scenario(context, scenario):
    """Set up a new browser page before each scenario."""
    context.page = context.browser_context.new_page()

def after_scenario(context, scenario):
    """Capture a screenshot on failure and close the page."""
    try:
        if scenario.status == "failed":
            screenshot_dir = "behave/reports/screenshots"
            os.makedirs(screenshot_dir, exist_ok=True)
            screenshot_path = f"{screenshot_dir}/{scenario.name}.png"
            if context.page:
                context.page.screenshot(path=screenshot_path)
    except Exception as e:
        print(f"Error taking screenshot: {e}")
    finally:
        try:
            if context.page and not context.page.is_closed():
                context.page.close()
        except Exception as e:
            print(f"Error closing page: {e}")

# def after_all(context):
#     """Close the browser and stop Playwright after all tests."""
#     try:
#         if context.browser:
#             context.browser.close()
#         if context.playwright:
#             context.playwright.stop()
#     except Exception as e:
#         print(f"Error closing browser: {e}")

def after_all(context):
    if hasattr(context, "browser_context"):
        context.browser_context.close()
    if hasattr(context, "browser"):
        context.browser.close()
    context.playwright.stop()