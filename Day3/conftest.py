import pytest
from playwright.sync_api import Page,expect

@pytest.fixture
def table_page(page: Page):
    page.set_default_navigation_timeout(60000)
    page.goto('https://demoqa.com/elements', wait_until='domcontentloaded')
    
    # moving to tables 
    page.get_by_text('Web Tables').click()
    page.locator('.ReactTable').scroll_into_view_if_needed()
    expect(page.get_by_role('heading',name='Web Tables')).to_be_visible()
    print('Landed on web tables!')
    
    return page

@pytest.fixture
def buttonPage(page: Page):
    page.goto('https://demoqa.com/buttons', wait_until='domcontentloaded')
    # page.locator('.ReactTable').scroll_into_view_if_needed()
    expect(page.get_by_role('heading',name='Buttons')).to_be_visible()
    print('We are on buttons page.')
    
    return page
    