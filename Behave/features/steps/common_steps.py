from behave import given, when, then
from playwright.sync_api import sync_playwright
from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@given("User login as '{username}' user")
def step_user_login(context, username):
    context.login_page = LoginPage(context.page)
    context.login_page.open()
    context.login_page.fill_credentials(username)
    context.login_page.submit_login()

