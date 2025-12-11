from playwright.sync_api import expect

def test_new_tab(browser_window):
    btn = browser_window.locator('#tabButton')
    with browser_window.context.expect_page() as tab:
        btn.click()
    new_tab = tab.value
    expect(new_tab, 'Not open in new tab...').to_have_url('https://demoqa.com/sample')
    new_tab.close()
    
def test_new_window(browser_window):
    btn = browser_window.locator('#windowButton')
    with context.expect_page('window') as n_win:
        