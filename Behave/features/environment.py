import sys,os
from playwright.sync_api import sync_playwright

# Add the Behave directory to Python path so step files can import pages, locators, utilities
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

def before_all(context):
    """Set up Playwright before all tests."""
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.webkit.launch(
        headless=False,
        slow_mo=1000,
        args=["--start-maximized"]
    )
    
def before_scenario(context, scenario):
    """Set up a new browser page before each scenario."""
    context.page = context.browser.new_page(no_viewport=True)
    
    # context.page = context.browser.new_page(viewport={'width': 1920, 'height': 1080})

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

def after_all(context):
    """Close the browser and stop Playwright after all tests."""
    try:
        if context.browser:
            context.browser.close()
        if context.playwright:
            context.playwright.stop()
    except Exception as e:
        print(f"Error closing browser: {e}")