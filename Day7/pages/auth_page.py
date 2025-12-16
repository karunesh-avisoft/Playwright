from playwright.sync_api import Page,expect
from dotenv import load_dotenv
import os
from utilities.common import logger
from locators.auth_locators import AuthPageLocators as L

load_dotenv()
# environment variables
base_url = os.getenv('BASE_URL')
standard = os.getenv('STANDARD_USER').strip("[]").replace('"', '').split(",")
passwd = os.getenv('PASSWORD')
inventory = os.getenv('INVENTORY_URL')

class AuthPage:
    def __init__(self, page:Page):
        self.page = page
    
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
        self.page.goto(base_url)
        logger.info('Asserting logo')
        expect(self.logo, "'Swag Labs' logo should be visible").to_be_visible()
        logger.info('On login page...')
    
    def fill_credentials(self, user):
        logger.info('Filling credentials')
        self.user_name.type(standard[user], delay=50)
        self.password.type(passwd, delay=50)
        
    def submit_login(self):
        logger.info('Logging in...')
        self.submit.click()
        
    
    def cross_error(self):
        self.cross_btn.click()
        logger.info('Closed error message')
        
    
    # ----------Assertions----------
    def assert_locked_out_error(self):
        expect(self.error_container).to_be_visible()
        expect(self.error_container).to_contain_text(
        "Epic sadface: Sorry, this user has been locked out."
    )
        