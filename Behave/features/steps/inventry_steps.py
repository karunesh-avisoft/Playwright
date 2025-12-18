from behave import given, when, then
from playwright.sync_api import sync_playwright
from pages.inventory_page import InventoryPage

@then("User navigates to the inventory page")
def user_should_be_on_inventory_page(context):
    context.inventory_page = InventoryPage(context.page)
    context.inventory_page.verify_open()
    context.inventory_page.take_screenshot("inventory_page")


@then("User should see 6 products listed")
def user_should_see_products(context):
    context.inventory_page.verify_products()


@when("User adds item '{item}' to the cart")
def step_add_item_to_cart(context, item):
    context.inventory_page.add_to_cart(item)


@when("User removes item '{item}' from the cart")
def step_remove_item_from_cart(context, item):
    context.inventory_page.remove_from_cart(item)


@when("User sorts items by '{sort_option}' sort_option")
def step_sort_items(context, sort_option):
    context.inventory_page.apply_sort(sort_option)


@then("The cart badge should show the correct number of items")
def step_verify_cart_badge(context):
    cart_count = context.inventory_page.cart_count
    context.inventory_page.assert_badge_count(cart_count)
    
@when("the user sorts products by <sort_option>")
def step_sort_products(context, sort_option):
    context.inventory_page.apply_sort(sort_option)

@then("the products should be sorted by '<sort_type>' order")
def step_verify_sorted_products(context, sort_type):
    context.inventory_page.assert_sort_order(sort_type)
    
@when("User logs out from the application")
def step_log_out(context):
    context.inventory_page.log_out()

@then("user should be redirected to the login page")
def step_verify_logout(context):
    context.inventory_page.assert_logout()