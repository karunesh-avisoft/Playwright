from playwright.sync_api import Page
from pages.auth_page import AuthPage
from pages.inventory_page import InventoryPage
import pytest

@pytest.fixture
def auth_page(page: Page):
    auth_user = AuthPage(page)
    auth_user.open()
    auth_user.fill_credentials(2)
    auth_user.submit_login()
    return auth_user

@pytest.fixture
def login(page: Page):
    def _login(user_id):
        auth = AuthPage(page)
        auth.open()
        auth.fill_credentials(user_id)
        auth.submit_login()
        return page
    return _login

@pytest.fixture
def inventory_page(auth_page, page:Page):
    inventory = InventoryPage(page)
    inventory.verify_open()
    inventory.verify_products()
    return inventory
