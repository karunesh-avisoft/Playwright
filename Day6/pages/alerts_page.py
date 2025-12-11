from playwright.sync_api import Page,expect
from locators.alerts_locator import AlertPageLocators as L
import logging

logger = logging.getLogger(__name__)

class AlertPage:
    def __init__(self, page:Page):
        self.page = page
    
    # Locators
    def locate(self, unique_loc):
        return self.page.locator(unique_loc)
    
    # Actions
    def open(self):
        self.page.goto('https://demoqa.com/alerts')
        logger.info('Verifying alerts page')
        # Accept any leftover dialogs BEFORE test runs
        # self.page.on("dialog", lambda dialog: dialog.dismiss())
        
        expect(self.page.locator("h1", has_text="Alerts")).to_be_visible()
        logger.info('Landed on alerts')
    
    def click_alert(self):
        def handle(dialog):
            logger.info(f"Message: {dialog.message}")
            # Assert dialog text
            assert dialog.type == 'alert', "Unexpected dialog"
            assert dialog.message == "You clicked a button", "Unexpected dialog"
            # Accept the dialog
            dialog.accept()
            logger.info('Alert accepted')
    
        self.page.once("dialog", handle)
        logger.info('Clicking alert button')
        self.locate(L.ALERT).click()
    
    def click_timer_alert(self):
        def handle(dialog):
            logger.info(f"Message: {dialog.message}")
            # Assert dialog text
            assert dialog.type == 'alert'
            assert dialog.message == "This alert appeared after 5 seconds", "Unexpected dialog"
            # Accept the dialog
            dialog.accept()
            logger.info('Timer alert accepted')
    
        self.page.once("dialog", handle)
        logger.info('Clicking timer alert button')
        self.locate(L.TIMER_ALERT).click()
         
    def click_dialog(self):
        self.page.wait_for_timeout(7000)
        def handle(dialog):
            logger.info(f"Message: {dialog.message}")
            # Assert dialog text
            assert dialog.type == 'confirm'
            assert dialog.message == "Do you confirm action?", "Unexpected dialog"
            # Accept the dialog
            dialog.dismiss()
            logger.info('Confirm alert dismissed')
    
        self.page.once("dialog", handle)
        logger.info('Clicking confirm dialog button')
        self.locate(L.DIALOG).click()
        
    def click_prompt(self):
        def handle(dialog):
            logger.info(f"Message: {dialog.message}")
            logger.info(f"Type: {dialog.type}")
            # Assert dialog text
            assert dialog.type == 'prompt'
            assert dialog.message == "Please enter your name", "Unexpected dialog"
            # Accept the dialog
            dialog.accept('Karunesh')
            logger.info('Prompt accepted')
    
        self.page.once("dialog", handle)
        logger.info('Clicking prompt button')
        self.locate(L.PROMPT).click()
        


        