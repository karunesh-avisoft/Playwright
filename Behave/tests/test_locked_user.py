from playwright.sync_api import Page
from pages.login_page import LoginPage


def test_locked_user_flow(page: Page):
    # ---------- AUTH ----------
    auth_user = LoginPage(page)
    auth_user.open()
    auth_user.fill_credentials("locked")
    auth_user.submit_login()
    auth_user.assert_locked_out_error()
