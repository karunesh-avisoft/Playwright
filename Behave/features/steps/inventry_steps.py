from behave import given, when, then
from pages.inventory_page import InventoryPage


@then("User navigates to the inventory page")
def user_should_be_on_inventory_page(context):
    context.inventory_page = InventoryPage(context.page)
    context.inventory_page.verify_open()


@then("User should see 6 products listed")
def user_should_see_products(context):
    context.inventory_page.verify_products()


@when("the user sorts products by '{sort_option}'")
def step_sort_products(context, sort_option):
    context.inventory_page.apply_sort(sort_option)


@then("the products should be sorted by '{sort_type}' order")
def step_verify_sorted_products(context, sort_type):
    context.inventory_page.assert_sort_order(sort_type)


@when("user logs out from the application")
def step_log_out(context):
    context.inventory_page.log_out()


@then("user should be redirected to the login page")
def step_verify_logout(context):
    context.inventory_page.assert_logout()
