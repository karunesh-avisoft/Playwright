from playwright.sync_api import Page, expect
import logging,os   
from locators.cart_checkout_locators import CartCheckoutLocators as L

# logger
logger = logging.getLogger(__name__)    

class CartPage:
    def __init__(self, page: Page):
        self.page = page

    # ----------Locators----------
    @property
    def cart_title(self):
        return self.page.locator(L.CART_TITLE)
    @property
    def cart_items(self):
        return self.page.locator(L.CART_ITEMS)
    @property
    def checkout(self):
        return self.page.locator(L.CHECKOUT)

    # ----------Actions----------
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