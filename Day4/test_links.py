from playwright.sync_api import expect

def test_link(links):
    with links.context.expect_page() as tab_info:
        links.locator("#dynamicLink").click()
    new_tab = tab_info.value
    # Verify new tab URL
    expect(new_tab).to_have_url("https://demoqa.com/")
    # Close new tab
    new_tab.close()
    # Original links is still open
    expect(links).to_have_url("https://demoqa.com/links")
    
    link_res = links.locator('#linkResponse')
    # created 201
    links.locator('#created').click()
    expect(link_res).to_contain_text('201')
    # no content 204
    links.locator('#no-content').click()
    expect(link_res).to_contain_text('204')
    # moved 301
    links.locator('#moved').click()
    expect(link_res).to_contain_text('301')
    # bad request 400
    links.locator('#bad-request').click()
    expect(link_res).to_contain_text('400')
    # unauthorized 401
    links.locator('#unauthorized').click()
    expect(link_res).to_contain_text('401')
    # forbidden 403
    links.locator('#forbidden').click()
    expect(link_res).to_contain_text('403')
    # not found 404
    links.locator('#invalid-url').click()
    expect(link_res, 'should return status code 404:NOT FOUND').to_contain_text('404')