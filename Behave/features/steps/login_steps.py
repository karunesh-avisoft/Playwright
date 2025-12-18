from behave import given, when, then
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage

@given('User on the login page')
def user_login_page(context):
    context.login_page = LoginPage(context.page)
    context.login_page.open()
    context.login_page.take_screenshot("login_page")

@when("User enters '{username}' as username")
def user_enter_credentials(context, username):
    context.login_page.fill_credentials(username)
    context.login_page.take_screenshot("after_credentials_filled")

@when('User submit the login form')
def user_submit_login_form(context):
    context.login_page.submit_login()

@then('User should see an error message indicating incorrect/incomplete credentials')
def user_should_see_error_message(context):
    context.login_page.assert_username_password()
    context.login_page.take_screenshot("login_error_message")