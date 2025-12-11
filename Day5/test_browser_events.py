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
    with browser_window.context.expect_page() as new_win:
        btn.click()
    print('Window: ', new_win)
    print('Window detail: ', new_win.value)
    window = new_win.value
    # assert new window
    expect(window.locator('h1', has_text='This is a sample page'), 'New window expected to be visible').to_be_visible()
    window.close()
    
    # assert the previous window
    expect(browser_window.locator('h1',has_text='Browser Windows')).to_be_visible()
    
def test_new_win_msg(browser_window):
    btn = browser_window.locator('#messageWindowButton')
    with browser_window.context.expect_page() as new_win:
        btn.click()
    window = new_win.value
    # assert new window
    expect(window.locator('body'), 'New window expected to have some text in the body/').to_have_text('Knowledge increases by sharing but not by saving. Please share this website with your friends and in your organization.')
    window.close()