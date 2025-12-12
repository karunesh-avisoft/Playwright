from pages.auth_page import AuthPage
from playwright.sync_api import Page
 
def test_auth(page:Page):
    auth_page = AuthPage(page)
    auth_page.open()
    auth_page.submit_login()    # in-complete submit
    
    auth_page.cross_error()
    
    auth_page.fill_credentials()
    
    auth_page.submit_login()
    