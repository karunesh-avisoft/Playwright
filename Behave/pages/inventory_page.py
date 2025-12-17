from playwright.sync_api import Page, expect
from pages.base_page import BasePage
from locators.inventory_locators import InventoryLocators as L
from utilities.test_data import TestData as TD
from utilities.common import logger, dialog_handler


class InventoryPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.product_names=[]
        self.product_prices=[]
        self.cart_count = 0
        self.tot_cart_prices = 0.0
    
    # ----------Locators----------
    @property
    def burger_menu(self):
        return self.page.locator(L.BURGER)
    @property
    def cross_button(self):
        return self.page.locator(L.CROSS)
    @property
    def filter(self):
        return self.page.locator(L.FILTER)
    @property
    def item_names(self):
        return self.page.locator(L.ITEM_NAMES)
    @property
    def item_prices(self):
        return self.page.locator(L.ITEM_PRICES)
    @property
    def cart_badge(self):
        return self.page.locator(L.CART_BADGE)
    @property
    def cart_container(self):
        return self.page.locator(L.CART_CONTAINER)
    @property
    def cart(self): 
        return self.page.locator(L.CART)
    @property
    def prod_images(self):
        return self.page.locator(L.INVENTORY_IMAGES)
    @property
    def logout(self):
        return self.page.locator(L.LOGOUT)

    # ----------Dynamic Locators----------
    def add(self, prod_name):
        return self.page.locator(f"{L.ADD_TO_CART}{prod_name}")
    
    def remove(self, prod_name):
        return self.page.locator(f"{L.REMOVE_FROM_CART}{prod_name}")
    
    
    # ----------Actions----------
    def get_product_names(self):
        return self.item_names.all_text_contents()
    
    def get_product_prices(self):
        prices = self.item_prices.all_text_contents()
        return [float(price.replace("$","")) for price in prices]
    
    def get_product_images(self):
        images = self.prod_images.all()
        return [img.get_attribute("src") for img in images]
        
    def verify_products(self):
        logger.info('Verifying products on inventory page')
        products = self.page.locator(L.PRODUCTS)
        expect(products, "Products should be available on inventory page").not_to_have_count(0)
        self.product_names = self.get_product_names()
        self.product_prices = self.get_product_prices()
        count = products.count()
        logger.info(f'Found {count} products on inventory page')    
        
    def verify_open(self):
        logger.info('Landing to inventory page')
        expect(self.page, "Should be on inventory page").to_have_url(TD.INVENTORY_URL)
        self.verify_products()
        logger.info('On inventory page...')
    
    def open_burger_menu(self):
        logger.info('Opening burger menu')
        self.burger_menu.click()
        expect(self.cross_button, "Cross button should be visible").to_be_visible()
        logger.info('Burger menu opened')
        
    def close_burger_menu(self):
        logger.info('Closing burger menu')
        self.cross_button.click()
        expect(self.burger_menu, "Burger menu button should be visible again").to_be_visible()
        logger.info('Burger menu closed')
        
        
    def apply_sort(self, value):
        self.filter.click()
        dialog_handler(self.page)       #dialog handler
        self.filter.select_option(value)
        logger.info(f'Applied sort: {value}')
                
        if value == 'az':
            names_az = self.get_product_names()
            expected = sorted(names_az)
            assert names_az == expected, "Products are not sorted A to Z"
            logger.info('Products sorted A to Z successfully')
        elif value == 'za':
            names_za = self.get_product_names()
            expected = sorted(names_za, reverse=True)
            assert names_za == expected, "Products are not sorted Z to A"
            logger.info('Products sorted Z to A successfully')
        elif value == 'lohi':
            prices_lohi = self.get_product_prices()
            expected = sorted(prices_lohi)
            assert prices_lohi == expected, "Products are not sorted Low to High"
            logger.info('Products sorted Low to High successfully')
        elif value == 'hilo':
            prices_hilo = self.get_product_prices()
            expected = sorted(prices_hilo, reverse=True)
            assert prices_hilo == expected, "Products are not sorted High to Low"
            logger.info('Products sorted High to Low successfully')
        
    # Adding and removing items from cart   
    def add_to_cart(self, idx):
        item_name = self.product_names[idx].replace(" ","-").lower()
        item_price = self.product_prices[idx]
        add_button = self.add(item_name)
        add_button.click()
        self.cart_count += 1
        self.tot_cart_prices += item_price
        logger.info(f'Added "{self.product_names[idx]}" to cart. Total items in cart: {self.cart_count}')
        # Assert item added
        assert self.cart_badge.text_content() == str(self.cart_count), "Cart badge count mismatch. Product may not be added."
            
    
    def remove_from_cart(self, idx):
        remove_button = self.remove(self.product_names[idx].replace(" ","-").lower())
        remove_button.click()
        self.cart_count -= 1
        self.tot_cart_prices -= self.product_prices[idx]
        logger.info(f'Removed "{self.product_names[idx]}" from cart. Total items in cart: {self.cart_count}')
        # Assert item removed
        assert self.cart_badge.text_content() == str(self.cart_count), "Cart badge count mismatch. Product may not be removed."
    
    def open_cart(self):
        logger.info('Opening cart page')
        self.cart.click()
        
    def product_image_mismatch(self):
        logger.info('Verify product image mismatch.')
        first_item = self.get_product_names()[0]
        first_image = self.get_product_images()[0]
        first_item = first_item.replace("Sauce Labs", "")
        
        assert first_item.lower() not in first_image.lower(), "Problem user should show mismatched product image"
        logger.info('Mismatch expected.')
    
    def log_out(self):
        self.open_burger_menu()
        self.logout.click()
        expect(self.page, 'User should logout.').to_have_url(TD.BASE_URL)
        logger.info('Logged out...')
            
            
    # ----------Assertions----------
    def assert_add_to_cart(self):
        assert self.cart_badge.text_content() == str(self.cart_count), "Cart badge count mismatch"
        
    def assert_problem_add_to_cart(self):
        assert self.cart_badge.text_content() != str(self.cart_count), "Cart badge count should mismatch"
        logger.info(f'Cart Badge count mismatch. There are {self.cart_badge.text_content()} items in cart.')
    
    def assert_hamburger(self):
        expect(self.page.locator('.bm-icon'), 'Hamburger should be a visual failure element.').to_contain_class('visual_failure')
        
    def assert_cross(self):
        expect(self.page.locator('.bm-cross'), 'Cross buttom should be a visual failure element.').to_contain_class('visual_failure')
        
    def assert_cart_btn(self):
        expect(self.cart_container, 'Cart buttom should be a visual failure element.').to_contain_class('visual_failure')