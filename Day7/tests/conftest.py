import pytest 
from playwright.sync_api import Page
from pages.auth_page import AuthPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

@pytest.fixture
def auth_page(page:Page):
    auth = AuthPage(page)
    auth.open()
    return auth

@pytest.fixture
def logged_in_page(page:Page, auth_page:AuthPage):
    auth_page.fill_credentials()
    auth_page.submit_login()
    return page 

@pytest.fixture
def inventory_page(logged_in_page:Page):
    inventory = InventoryPage(logged_in_page)
    inventory.verify_open()
    return inventory

@pytest.fixture
def add_items_to_cart(inventory_page:InventoryPage):
    addtocart = CartPage(inventory_page)
    
