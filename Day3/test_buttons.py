from playwright.sync_api import expect

def test_dblclick(buttonPage):
    button = buttonPage.locator('#doubleClickBtn')
    button.dblclick()
    # expected message 
    expect(buttonPage.locator('#doubleClickMessage')).to_be_visible()
    print('Double click button')
    buttonPage.pause()
    
def test_right_click(buttonPage):
    button = buttonPage.locator('#rightClickBtn')
    button.click(button='right')
    # expected message 
    expect(buttonPage.locator('#rightClickMessage')).to_be_visible()
    print('Right click button')
    buttonPage.pause()

def test_dynamicId(buttonPage):
    button = buttonPage.get_by_role('button', name='Click Me', exact=True)
    button.click()
    # expected message 
    expect(buttonPage.locator('#dynamicClickMessage')).to_be_visible()
    print('Dynamic click button')
    buttonPage.pause()