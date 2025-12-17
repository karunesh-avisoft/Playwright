from behave import given, when, then
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
import allure

@given('User on the login page')
def user_on_login_page(context):
    context.login_page = LoginPage(context.page)
    context.login_page.open()
    context.login_page.take_screenshot("login_page")

@when("User enter '{username}' and password")
def user_enter_credentials(context, username):
    context.login_page.fill_credentials(username)

@when('User submit the login form')
def user_submit_login_form(context):
    context.login_page.submit_login()
    context.login_page.take_screenshot("after_login")
    
@then('User should be logged in successfully')
def user_should_be_logged_in_successfully(context):
    context.inventory_page = InventoryPage(context.page)
    context.inventory_page.verify_open()
    context.inventory_page.take_screenshot("inventory_page")