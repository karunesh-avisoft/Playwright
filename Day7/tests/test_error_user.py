from playwright.sync_api import Page
from pages.auth_page import AuthPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage

def test_remove_added_items(login, page: Page):
    
    # ---------- AUTH ----------
    login(4)
    
    inventory = InventoryPage(page)
    
    