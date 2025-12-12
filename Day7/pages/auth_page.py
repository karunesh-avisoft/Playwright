from playwright.sync_api import Page,expect
from dotenv import load_dotenv
import os
import logging
from locators.auth_locators import AuthPageLocators as L

load_dotenv()
# environment variables
base_url = os.getenv('BASE_URL')
standard = os.getenv('STANDARD_USER').strip("[]").replace('"', '').split(",")
passwd = os.getenv('PASSWORD')
inventory = os.getenv('INVENTORY_URL')

# logger
logger = logging.getLogger(__name__)

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
    
    def fill_credentials(self):
        logger.info('Filling credentials')
        self.user_name.type(standard[0], delay=50)
        self.password.type(passwd, delay=50)
        
    def submit_login(self):
        logger.info('Logging in...')
        self.submit.click()
        # logger.info('Assert entries')
        # expect(self.error_container, "Should have entered valid data.").not_to_be_visible()
    
    def cross_error(self):
        self.cross_btn.click()
        logger.info('Closed error message')
        