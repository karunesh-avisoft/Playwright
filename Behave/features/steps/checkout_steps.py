from behave import given, when, then
from pages.checkout_page import CheckoutPage


@then("User should be navigated to the checkout page")
def step_verify_checkout_page(context):
    context.checkout_page = CheckoutPage(context.page)
    context.checkout_page.verify_open()


@when("User clicks Cancel on overview")
def step_click_cancel(context):
    context.checkout_page.cancel_checkout()


@then("User continue from checkout overview")
def step_continue_from_checkout(context):
    context.checkout_page.continue_checkout()


@then("Error: Last Name is required should be displayed")
def step_verify_last_name_error(context):
    context.checkout_page.assert_lastname()
