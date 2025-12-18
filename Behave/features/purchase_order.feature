Feature: Purchase Order Flow

	Background: User logged in and on inventory page
		Given User login as 'standard' user
		Then User navigates to the inventory page

	Scenario: Successful completion of purchase order
		When User adds item 'backpack' to the cart
		And User adds item 'fleece jacket' to the cart
		And User clicks on the cart icon
		And User proceeds to checkout
		And User fills checkout details with first name:'John', last name:'Doe', and postal code:'12345'
		And User continues to overview and verify total amount as well as finishes the order
		Then User should see the order confirmation page with message Thank you for your order!
