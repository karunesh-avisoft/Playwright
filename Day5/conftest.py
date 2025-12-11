import pytest
from playwright.sync_api import Page,expect

@pytest.fixture
def practice_form(page:Page):
    page.set_default_navigation_timeout(60000)
    page.goto('https://demoqa.com/automation-practice-form')
    # verifying the page
    expect(page.locator('h1',has_text='Practice Form')).to_be_visible()
    page.locator('.practice-form-wrapper').scroll_into_view_if_needed()
    return page

@pytest.fixture
def browser_window(page:Page):
    page.set_default_navigation_timeout(60000)
    page.goto('https://demoqa.com/browser-windows')
    # verifying the page
    expect(page.locator('h1',has_text='Browser Windows')).to_be_visible()
    return page