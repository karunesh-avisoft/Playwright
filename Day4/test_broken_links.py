from playwright.sync_api import expect

def test_valid_img(broken):
    valid_img = broken.locator('img[src="/images/Toolsqa.jpg"]').nth(0)
    broken_img = broken.locator('img[src="/images/Toolsqa_1.jpg"]')
    
    assert valid_img.evaluate('img => img.naturalWidth>0'), "Valid image did not load"
    assert broken_img.evaluate('img => img.naturalWidth==0'), "Broken image unexpectedly loaded"

def test_valid_link(broken):
    valid_link = broken.locator("text='Click Here for Valid Link'")
    with broken.expect_navigation():
        valid_link.click()
        
    expect(broken, "Didn't redirect").to_have_url("https://demoqa.com/")
    broken.go_back()
    broken_link = broken.locator("text='Click Here for Broken Link'")
    with broken.expect_navigation():
        broken_link.click()
    expect(broken, "Didn't redirect to broken page").to_have_url('http://the-internet.herokuapp.com/status_codes/500')
    