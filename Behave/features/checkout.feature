Feature: Checkout Page

	Background: User logged in as problem user and on inventory page
		Given User login as 'problem' user
		Then User navigates to the inventory page
		When User adds item 'backpack' to the cart
		And User adds item 'Onesie' to the cart
		And User clicks on the cart icon
		And User proceeds to checkout page
    
	Scenario: Cancel checkout
		When User fills checkout details with first name:'John', last name:'Problem', and postal code:'12345'
		And User clicks Cancel on overview
		Then User navigates to the cart page
		And The cart badge should show the correct number of items

	Scenario: Error on empty checkout fields
		When User fills checkout details with first name:'John', last name:'Problem', and postal code:'12345'
		Then User continue from checkout overview
		And Error: Last Name is required should be displayed