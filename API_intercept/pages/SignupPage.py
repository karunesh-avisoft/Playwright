from playwright.sync_api import Page, expect
class SignupPage:
    def __init__(self, page: Page):
        self.page = page
        # ========== LOCATORS ==========
        # self.email_input = self.page.locator('//input[@id="_r_6_-form-item"]')
        self.email_input = self.page.locator('//input[@name="email"]')
        self.otp_input_locator = self.page.locator('//div[@class="flex gap-2 undefined"]/input')
        self.get_otp_button = self.page.get_by_role("button", name="GET OTP")
        self.verify_button  = self.page.locator('//button[text()="VERIFY"]')
        self.mobile_number_input = self.page.get_by_label('Mobile')
        
        
    # ========== ACTIONS ==========
    def open(self):
        self.page.goto('https://staging-mf-partners.vercel.app/register/mfd')
        
    # Email
    def enter_email(self, email):
        self.email_input.type(email)
    
    def click_get_otp(self, n=0):
        self.get_otp_button.nth(n).click()
        
    def enter_otp(self, otp):
        for i,digit in enumerate(otp):
            self.otp_input_locator.nth(i).type(digit)
    
    def click_verify_button(self):
        self.verify_button.click()
        
    # Mobile Number
    def enter_mobile_number(self, mobile_number):
        self.mobile_number_input.type(mobile_number)
    

    
    # ========== ASSERTONS ==========
    def verify_signup_page(self):
        expect(self.page, 'User should be on signup page!').to_have_url('https://staging-mf-partners.vercel.app/register/mfd')
    
    