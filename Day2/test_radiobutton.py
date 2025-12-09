from playwright.sync_api import Page, expect

def test_radiobutton(page:Page):
    page.set_default_navigation_timeout(60000)
    page.goto("https://demoqa.com/elements", wait_until='domcontentloaded')
    print(f"Title: {page.title()}")

    radio_button = page.get_by_text("Radio Button")
    radio_button.click()
    expect(page.get_by_role('heading', name='Radio Button')).to_be_visible()
    print('Landed on the radio button page')

    # locate impressive radio button
    # radio_button = page.locator("//input[@id='impressiveRadio']")
    page.get_by_text("Impressive").click()
    print('Impressive selected...')
    page.pause()
    # expecting the result text containing 'Impressive'
    result = page.locator('.text-success')
    expect(result).to_contain_text("Impressive")
    print('Impressive found')
    page.pause()