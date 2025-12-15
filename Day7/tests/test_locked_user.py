from playwright.sync_api import Page
from pages.auth_page import AuthPage


def test_locked_user_flow(page: Page):
    # ---------- AUTH ----------
    auth_user = AuthPage(page)
    auth_user.open()
    auth_user.fill_credentials(1)
    auth_user.submit_login()
    auth_user.assert_locked_out_error()
