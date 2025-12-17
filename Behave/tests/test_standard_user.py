from playwright.sync_api import Page
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_standard_user_item_purchase_flow(login, page: Page):
    # ---------- AUTH ----------
    login("standard")
    # ---------- INVENTORY ----------
    inventory_page = InventoryPage(page)
    inventory_page.verify_open()

    inventory_page.open_burger_menu()
    inventory_page.close_burger_menu()

    # Sorting checks
    # inventory_page.apply_sort("az")
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
    # Back to inventory
    checkout_page.back_to_home()
    
    inventory_page.verify_open()
    # Logout
    inventory_page.log_out()
