from playwright.sync_api import Page
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utilities.common import measure


def test_peformance_user_flow(login,page: Page):
    # ---------- AUTH ----------
    login_time = measure(
        lambda: (login("performance"))
    )
    # Expect slow login
    assert login_time > 3, f"Login too fast: {login_time}s"

    # ---------- INVENTORY ----------
    inventory_page = InventoryPage(page)

    inventory_page.verify_open()

    inventory_page.open_burger_menu()
    inventory_page.close_burger_menu()

    # Sorting performance
    sort_time = measure(lambda: inventory_page.apply_sort("hilo"))
    # Expect slow sorting
    assert sort_time > 3, f"Sorted early in {sort_time}s"

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
    back_home_time = measure(lambda: checkout_page.back_to_home())
    assert back_home_time > 1, f"Early back to inventory in {back_home_time}s"
    
    inventory_page.verify_open()
    # Logout
    inventory_page.log_out()

