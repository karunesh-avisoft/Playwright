from playwright.sync_api import Page

def test_api_get(playwright, page:Page):
    request = playwright.request.new_context()
    response = request.get('https://jsonplaceholder.typicode.com/posts/1')
    
    assert response.status == 200
    data = response.json()
    print(data)
    page.goto('https://jsonplaceholder.typicode.com')
    response = page.waitForResponse('**/posts/1')
    
    assert response.status == 200
    data = response.json()
    print(data)
    
    request.dispose()
    
    # pytest .\test_api_get.py -s