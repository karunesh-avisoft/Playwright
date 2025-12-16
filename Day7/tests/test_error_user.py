from playwright.sync_api import Page
from pages.auth_page import AuthPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from utilities.common import logger


def test_add_items(login, page: Page):
    login(4)

    inventory = InventoryPage(page)
    inventory.verify_open()

    inventory.add_to_cart(0)
    # Expect add error
    inventory.add_to_cart(2)


def test_remove_added_items(login, page: Page):
    login(4)

    inventory = InventoryPage(page)
    inventory.verify_open()

    inventory.add_to_cart(0)
    # Expect removal error
    inventory.remove_from_cart(0)


def test_sorting(login, page: Page):
    login(4)

    inventory = InventoryPage(page)

    # Expect a dialog with msg
    inventory.apply_sort("lohi")


def test_checkout_form(login, page: Page):
    login(4)
    inventory = InventoryPage(page)
    inventory.verify_open()
    inventory.add_to_cart(0)
    inventory.add_to_cart(1)
    inventory.open_cart()

    cart = CartPage(page)
    cart.proceed_to_checkout()

    checkout = CheckoutPage(page)
    checkout.fill_checkout_details()
    checkout.assert_checkout_details()
    checkout.continue_checkout()


def test_finish_enable(login, page: Page):
    login(4)
    inventory = InventoryPage(page)
    inventory.verify_open()
    inventory.add_to_cart(0)
    inventory.add_to_cart(1)
    inventory.open_cart()

    cart = CartPage(page)
    cart.proceed_to_checkout()

    checkout = CheckoutPage(page)
    checkout.fill_checkout_details()
    checkout.continue_checkout()

    # Expect disabled finish
    checkout.assert_finish_button()
    checkout.finish_checkout()
