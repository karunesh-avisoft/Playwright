from playwright.sync_api import Page,expect
import pytest
import logging

logger = logging.getLogger(__name__)

class FramePage:
    def __init__(self, page:Page):
        self.page = page
        
    # locator
    def locate(self, unique):
        return self.page.locator(unique)
    
    # Actions
    def open(self):
        self.page.goto('https://demoqa.com/frames', wait_until='domcontentloaded')
        
        # assert page
        expect(self.page.locator('h1')).to_be_visible()
    
    