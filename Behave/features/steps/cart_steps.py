from behave import given, when, then
from pages.cart_page import CartPage


@when("User clicks on the cart icon")
def step_click_cart_icon(context):
    context.inventory_page.open_cart()
    context.cart_page = CartPage(context.page)
    
@then("User navigates to the cart page")
def step_verify_on_cart(context):
    context.cart_page.verify_open()


@when("User proceeds to checkout page")
def step_procced_to_checkout(context):
    context.cart_page.proceed_to_checkout()


@when("User adds item '{item}' to the cart")
def step_add_item_to_cart(context, item):
    context.inventory_page.add_to_cart(item)


@when("User removes item '{item}' from the cart")
def step_remove_item_from_cart(context, item):
    context.inventory_page.remove_from_cart(item)


@then("The cart badge should show the correct number of items")
def step_verify_cart_badge(context):
    context.inventory_page.assert_badge_count(context.inventory_page.cart_count)


@then("User verify the items in cart")
def step_verify_item_in_cart(context):
    context.cart_page.verify_cart_items(context.inventory_page.cart_count)
