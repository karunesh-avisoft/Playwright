from playwright.sync_api import Page
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_visual_user_flow(login,page: Page):
    # ---------- AUTH ----------
    login("visual")
    # ---------- INVENTORY ----------
    inventory_page = InventoryPage(page)
    inventory_page.verify_open()

    inventory_page.open_burger_menu()
    inventory_page.assert_hamburger()      #Expect UI error
    inventory_page.close_burger_menu()
    inventory_page.assert_cross()           #Expect UI error

    # Items to cart
    inventory_page.add_to_cart(0)
    inventory_page.add_to_cart(3)
    inventory_page.add_to_cart(4)
    inventory_page.remove_from_cart(3)

    # ---------- CART ----------
    inventory_page.assert_cart_btn()        #Expect UI error
    inventory_page.open_cart()

    cart_page = CartPage(page)
    cart_page.verify_open()

    # ---------- CHECKOUT ----------
    cart_page.assert_checkout_btn()         #Expect UI error
    cart_page.proceed_to_checkout()

    checkout_page = CheckoutPage(page)
    # Verify checkout page one
    checkout_page.verify_open()
    checkout_page.fill_checkout_details()
    checkout_page.continue_checkout()

    # Verify checkout page two
    checkout_page.verify_checkout_overview()
    checkout_page.finish_checkout()

    # Verify order completion
    checkout_page.verify_order_completion()
    # Back to inventory
    checkout_page.back_to_home()
    
    inventory_page.verify_open()
    # Logout
    inventory_page.log_out()
