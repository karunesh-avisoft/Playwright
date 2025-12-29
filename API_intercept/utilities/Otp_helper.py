from playwright.sync_api import Route

def captureOTP(page, signup_page, n=0):
    endpoint = "**/api/v1/" + "partner_credentials_otp"
    # otp_value = {}

    # # Event-driven capture
    # def handle_otp_route(route: Route):
    #     # Let the request go through
    #     response = route.fetch()
    #     data = response.json()
    #     otp_value["otp"] = data["data"]["OTP"]
    #     # Continue with original response
    #     route.fulfill(response=response)

    # # Intercept OTP API BEFORE triggering the request
    # page.route("**/api/v1/partner_credentials_otp", handle_otp_route)
    
    
    # Wait for the network request and capture OTP
    with page.expect_response(endpoint) as resp_info:
        signup_page.click_get_otp(n)

    # Extract OTP from the response
    response = resp_info.value
    json_data = response.json()
    otp = json_data["data"]["OTP"]
    return otp  