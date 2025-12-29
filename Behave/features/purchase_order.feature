Feature: Successfull Purchase Order Flow

	Background: User logged in as standard user and on inventory page
		Given User login as 'standard' user
		Then User navigates to the inventory page

	@purchase_order
	Scenario: Successful completion of purchase order
		When User adds item 'Onesie' to the cart
		And User adds item 'fleece jacket' to the cart
		And User clicks on the cart icon
		And User proceeds to checkout page
		And User fills checkout details with first name:'John', last name:'Doe', and postal code:'12345'
		Then User continue from checkout overview
		When User verifies total amount as well as finishes the order
		Then User should see the order confirmation page with message Thank you for your order!


