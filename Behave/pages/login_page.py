from playwright.sync_api import Page, expect
from pages.base_page import BasePage
from utilities.test_data import TestData as TD
from utilities.common import logger
from locators.auth_locators import AuthPageLocators as L
from utilities.credentials import get_user, get_passwd


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    # ----------Locators----------
    @property
    def logo(self):
        return self.page.locator(L.LOGO)

    @property
    def user_name(self):
        return self.page.locator(L.USER_NAME)

    @property
    def password(self):
        return self.page.locator(L.PASSWORD)

    @property
    def submit(self):
        return self.page.locator(L.SUBMIT)

    @property
    def error_container(self):
        return self.page.locator(L.ERROR)

    @property
    def cross_btn(self):
        return self.page.locator(L.CROSS_ERROR)

    # ----------Actions----------
    def open(self):
        self.page.goto(TD.BASE_URL)
        logger.info("Asserting logo")
        expect(self.logo, "'Swag Labs' logo should be visible").to_be_visible()
        logger.info("On login page...")

    def fill_credentials(self, user_key: str):
        logger.info("Filling credentials")
        user = get_user(user_key)
        if user is None:
            user = user_key
        self.user_name.type(user)
        self.password.type(get_passwd() or "secret_sauce")

    def submit_login(self):
        logger.info("Logging in...")
        self.submit.click()

    def cross_error(self):
        self.cross_btn.click()
        logger.info("Closed error message")

    # ----------Assertions----------
    def assert_username_password(self):
        expect(self.error_container).to_be_visible()
        assert (
            "username"
            or "Password"
            or "Username and password" in self.error_container.inner_text()
        ), "Error message should mention missing username or password"

    def assert_locked_out_error(self):
        expect(self.error_container).to_be_visible()
        expect(self.error_container).to_contain_text(
            "Epic sadface: Sorry, this user has been locked out."
        )
