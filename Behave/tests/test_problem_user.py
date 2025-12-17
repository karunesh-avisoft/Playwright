from playwright.sync_api import Page
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_add_to_cart(login, page: Page):
    login('problem')
    inventory_page = InventoryPage(page)
    inventory_page.verify_open()
    
    # Item name and image mismatch
    inventory_page.product_image_mismatch()
    
    inventory_page.add_to_cart(1)
    inventory_page.add_to_cart(2)
    inventory_page.add_to_cart(3)
    # AssertionError: Cart badge count mismatch
    
def test_remove_from_cart(login, page: Page):
    login('problem')
    inventory_page = InventoryPage(page)
    inventory_page.verify_open()
    # ---------- Inventory ----------
    inventory_page.add_to_cart(1)
    inventory_page.remove_from_cart(1)
    
def test_sorting_inventory(login, page: Page):
    login('problem')
    inventory_page = InventoryPage(page)
    inventory_page.verify_open()
    inventory_page.apply_sort('za')
    
def test_checkout_details(login, page: Page):
    login('problem')
    inventory_page = InventoryPage(page)
    inventory_page.verify_open()
    inventory_page.add_to_cart(1)
    inventory_page.add_to_cart(0)
    inventory_page.open_cart()
    
    # ---------- Checkout ----------
    cart_page = CartPage(page)
    cart_page.verify_open()
    cart_page.verify_cart_items(inventory_page.cart_count)
    cart_page.proceed_to_checkout()
    
    checkout_page = CheckoutPage(page)
    checkout_page.verify_open()
    
    checkout_page.fill_checkout_details()
    checkout_page.continue_checkout()
    checkout_page.assert_lastname()