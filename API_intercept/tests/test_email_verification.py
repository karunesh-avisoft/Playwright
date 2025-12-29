from playwright.sync_api import Page, Route
from pages.SignupPage import SignupPage
from utilities.Otp_helper import captureOTP

def test_email_mobile_verification(page: Page):
    signup_page = SignupPage(page)
    signup_page.open()
    
    # Email Verification
    signup_page.enter_email("abc123@gmail.com")

    otp = captureOTP(page, signup_page) # email otp capture

    signup_page.enter_otp(str(otp))
    signup_page.click_verify_button()
    
    # Mobile Number Verification
    signup_page.enter_mobile_number("9876543218")
    
    otp = captureOTP(page, signup_page) # mobile otp capture
    
    signup_page.enter_otp(str(otp))
    signup_page.click_verify_button()