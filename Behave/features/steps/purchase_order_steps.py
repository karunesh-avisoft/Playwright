from behave import given, when, then
from playwright.sync_api import sync_playwright
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@when("User clicks on the cart icon")
def step_click_cart_icon(context):
    context.inventory_page.open_cart()
    
@when("User proceeds to checkout")
def step_procced_to_checkout(context):
    context.cart_page = CartPage(context.page)
    context.cart_page.proceed_to_checkout()

@when("User fills checkout details with first name:'{first_name}', last name:'{last_name}', and postal code:'{postal_code}'")
def step_fill_checkout_details(context, first_name, last_name, postal_code):
    context.checkout_page = CheckoutPage(context.page)
    context.checkout_page.fill_checkout_details(first_name, last_name, postal_code)

@when("User continues to overview and verify total amount as well as finishes the order")
def step_continue_and_finish_order(context):
    context.checkout_page.continue_checkout()
    context.checkout_page.verify_checkout_overview()
    context.checkout_page.verify_total_amount(context.inventory_page.tot_cart_prices)
    context.checkout_page.finish_checkout()

@then("User should see the order confirmation page with message Thank you for your order!")
def user_should_see_order_confirmation(context):
    context.checkout_page.verify_order_completion()