
def test_api_get(playwright):
    request = playwright.request.new_context()
    response = request.get('https://jsonplaceholder.typicode.com/posts/1')
    
    assert response.status == 200
    data = response.json()
    print(data)
    
    request.dispose()
    
    # pytest .\test_api_get.py -s