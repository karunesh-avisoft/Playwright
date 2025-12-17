from playwright.sync_api import Page
from pages.login_page import LoginPage
import pytest

@pytest.fixture
def login(page: Page):
    def _login(user_key):
        auth = LoginPage(page)
        auth.open()
        auth.fill_credentials(user_key)
        auth.submit_login()
        return page
    return _login

