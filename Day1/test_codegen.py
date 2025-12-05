import re
from playwright.sync_api import Page, expect


def test_banner(page: Page) -> None:
    page.goto("https://demoqa.com/text-box")
    page.get_by_role("link").click()
    expect(page.get_by_role("link", name="Selenium Online Training")).to_be_visible()


def test_codegen(page: Page) -> None:
    page.goto("https://playwright.dev/")
    page.get_by_role("button", name="Node.js").click()
    page.get_by_label("Main", exact=True).get_by_role("link", name="Python").click()
    page.get_by_role("link", name="Get started").click()
    page.get_by_role("link", name="Generating tests").click()
    expect(page.locator("h1")).to_contain_text("Generating tests")
