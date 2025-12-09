import pytest
from playwright.sync_api import Page,expect

@pytest.fixture
def links(page:Page):
    page.set_default_navigation_timeout(60000)
    page.goto('https://demoqa.com/links')
    wrapper = page.locator('#linkWrapper')
    expect(wrapper).to_be_visible()
    wrapper.scroll_into_view_if_needed()
    return page

@pytest.fixture
def broken(page: Page):
    page.goto('https://demoqa.com/broken')
    expect(page.get_by_role('heading', name='Broken Links - Images')).to_be_visible()
    return page

@pytest.fixture
def files(page:Page):
    page.goto('https://demoqa.com/upload-download')
    expect(page).to_have_url('https://demoqa.com/upload-download')
    return page

@pytest.fixture
def x_path(page:Page):
    page.goto('https://www.knowledgeware.in/Automation/web.html#')
    expect(page.locator('#textb')).to_have_text('X-Path')
    return page