from playwright.sync_api import Page, expect  
from pages.base_page import BasePage
from locators.cart_checkout_locators import CartCheckoutLocators as L
from utilities.common import logger 

class CartPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    # ---------- Locators ----------
    @property
    def cart_title(self):
        return self.page.locator(L.CART_TITLE)
    @property
    def cart_items(self):
        return self.page.locator(L.CART_ITEMS)
    @property
    def checkout(self):
        return self.page.locator(L.CHECKOUT)

    # ---------- Actions ----------
    def verify_open(self):
        logger.info('Verifying cart page is open')
        expect(self.cart_title).to_have_text('Your Cart')
        logger.info('Cart page is open')
        
    def verify_cart_items(self, expected_count:int):
        logger.info(f'Verifying cart has {expected_count} items')
        actual_count = self.cart_items.count()
        assert actual_count == expected_count, f"Expected {expected_count} items in cart, found {actual_count}"
        logger.info('Cart items verified')    
    
    def proceed_to_checkout(self):
        logger.info('Proceeding to checkout')
        self.checkout.click()
        
    # ---------- Assertions ----------
    def assert_checkout_btn(self):
        expect(self.checkout, 'Checkout buttom should be a visual failure element.').to_contain_class('btn_visual_failure')