from playwright.sync_api import Page
from pages.auth_page import AuthPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_standard_user_flow(page: Page):
    # ---------- AUTH ----------
    auth_page = AuthPage(page)
    auth_page.open()

    # Verify error on empty submit
    auth_page.submit_login()
    auth_page.cross_error()

    # Login successfully
    auth_page.fill_credentials(0)
    auth_page.submit_login()

    # ---------- INVENTORY ----------
    inventory_page = InventoryPage(page)
    inventory_page.verify_open()

    inventory_page.open_burger_menu()
    inventory_page.close_burger_menu()

    inventory_page.verify_products()

    # Sorting checks
    inventory_page.apply_sort("az")
    inventory_page.apply_sort("za")
    inventory_page.apply_sort("lohi")
    inventory_page.apply_sort("hilo")

    # Items to cart
    inventory_page.add_to_cart(0)
    inventory_page.add_to_cart(3)
    inventory_page.add_to_cart(4)
    inventory_page.remove_from_cart(3)

    cart_count = inventory_page.cart_count
    total_cart_prices = inventory_page.tot_cart_prices

    # ---------- CART ----------
    inventory_page.open_cart()

    cart_page = CartPage(page)
    cart_page.verify_open()
    # Verify cart items
    cart_page.verify_cart_items(expected_count=cart_count)

    # ---------- CHECKOUT ----------
    cart_page.proceed_to_checkout()

    checkout_page = CheckoutPage(page)
    # Verify checkout page one
    checkout_page.verify_open()
    checkout_page.fill_checkout_details()
    checkout_page.continue_checkout()

    # Verify checkout page two
    checkout_page.verify_checkout_overview()
    checkout_page.verify_total_amount(total_cart_prices)
    checkout_page.finish_checkout()

    # Verify order completion
    checkout_page.verify_order_completion()
