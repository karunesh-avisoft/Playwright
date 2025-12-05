import re
from playwright.sync_api import Page, expect

def test_has_banner(page:Page):
    page.set_default_navigation_timeout(60000)  # 60 seconds
    # goto this page
    page.goto('https://demoqa.com/elements')
    
    # click the nav image
    page.locator("//div[@id='app']//header//a").click()
    page.pause()
    # expects page has a banner with name 'Selenium Online Training'
    expect(page.locator("//div[@class='home-banner']")).to_be_visible()

def test_form(page: Page):
    page.set_default_navigation_timeout(60000)  # 60 seconds
    page.goto("https://demoqa.com/text-box")
    
    # fullname
    fullname = page.get_by_role('textbox', name="Full Name")
    fullname.fill('Karunesh Tiwari')
    expect(fullname).to_have_value('Karunesh Tiwari')
    # email
    email = page.get_by_role('textbox', name="name@example.com")
    email.fill('karunesh@gmail.com')
    expect(email).to_have_value('karunesh@gmail.com')
    # current add
    curr_add = page.get_by_role('textbox', name="Current Address")
    curr_add.fill('abc,12345,Jammu')
    expect(curr_add).to_have_value('abc,12345,Jammu')
    # permanent add
    per_add = page.locator('#permanentAddress')
    per_add.fill('abc,12345,Jammu')
    expect(per_add).to_have_value('abc,12345,Jammu')
    
    page.get_by_role('button').click()
    
    expect(page.locator('#output')).to_be_visible()
    page.pause()
    
    
    
