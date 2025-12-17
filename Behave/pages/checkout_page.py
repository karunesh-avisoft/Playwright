from playwright.sync_api import Page, expect
import  re
from pages.base_page import BasePage
from locators.cart_checkout_locators import CartCheckoutLocators as L  
from utilities.common import logger
from utilities.test_data import TestData as TD

class CheckoutPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)  

    # ----------Locators----------
    @property
    def first_name_input(self):
        return self.page.locator(L.FIRSTNAME)
    @property
    def last_name_input(self):
        return self.page.locator(L.LASTNAME)
    @property
    def postal_code_input(self):
        return self.page.locator(L.POSTALCODE)
    @property
    def continue_button(self):
        return self.page.locator(L.CONTINUE)
    @property
    def title(self):
        return self.page.locator(L.TITLE)
    @property
    def finish_button(self):
        return self.page.locator(L.FINISH)
    @property
    def complition_msg(self):
        return self.page.locator(L.COMPLETE_HEADING)
    @property
    def error_container(self):
        return self.page.locator(L.ERROR)
    @property
    def back_home(self):
        return self.page.locator(L.BACK_HOME)

    # ----------Actions----------
    def verify_open(self):
        logger.info('Verifying checkout page is open')
        expect(self.page).to_have_url(TD.CHECKOUT_URL)
        logger.info('Checkout page is open')
        
    def fill_checkout_details(self):
        logger.info('Filling checkout information')
        self.first_name_input.type(TD.FIRST_NAME)
        self.last_name_input.type(TD.LAST_NAME)
        self.postal_code_input.press_sequentially(TD.POSTAL_CODE)

    def continue_checkout(self):
        logger.info('Submitting checkout information')
        self.continue_button.click()
        
    def verify_checkout_overview(self):
        logger.info('Verifying checkout overview page is open')
        expect(self.title).to_contain_text('Overview')
    
    def verify_total_amount(self, total_item_amt: str):
        logger.info('Verifying total amount on checkout overview page')
        total_text = self.page.locator(L.TOTAL).text_content()
        total_price = float(re.search(r'([\d]+\.\d{2})', total_text).group(1))
        # Tax addition at 0.08
        tax = total_item_amt*float(TD.TAX_RATE)
        expected_total = round(total_item_amt + tax, 2)
        assert expected_total == total_price, f"Expected total '{expected_total}' not found in '{total_price}'"
        logger.info('Total amount verified successfully')
    
    def finish_checkout(self):
        logger.info('Finishing checkout process')
        self.finish_button.click()
        
    def verify_order_completion(self):
        expect(self.complition_msg).to_contain_text('Thank you for your order')
        logger.info('Order completed successfully')
    
    def back_to_home(self):
        self.back_home.click()
        
    # ---------- Assertions ----------
    def assert_lastname(self):
        expect(self.error_container).to_be_visible()
        expect(self.error_container, "Error: Last Name is required").not_to_have_text('Error: Last Name is required')
        self.page.pause()
        
    def assert_checkout_details(self):
        expect(self.last_name_input, 'Should have last name.').to_have_text(lastname)
        expect(self.first_name_input, 'Should have first name.').to_have_text(firstname)
        expect(self.last_name_input, 'Should have postal code.').to_have_text(postalcode)
        
    def assert_finish_button(self):
        expect(self.page,"Navigation to order completion stopped for error user.").to_have_url(TD.CHECKOUT_URL)