Feature: Inventory Page Validations

	Background: User logged in and on inventory page
		Given User login as 'standard' user
		Then User navigates to the inventory page

	Scenario: Verify available products on inventory page
		Then User should see 6 products listed

	Scenario: Verify cart badge updates after adding items
		When User adds item 'bolt t-shirt' to the cart
		Then The cart badge should show the correct number of items

	Scenario: Verify cart badge updates after removing items
		When User adds item 'bike light' to the cart
		And User adds item 'bolt t-shirt' to the cart
		And User removes item 'bike light' from the cart
		Then The cart badge should show the correct number of items
    
	Scenario Outline: Sort products by different options
		When the user sorts products by '<sort_option>'
		Then the products should be sorted by '<sort_type>' order

		Examples:
			| sort_option             | sort_type     |
			| az                    | name ascending|
			| za                    | name descending|
			| lohi                  | price ascending|
			| hi                    | price descending|

	Scenario: Logout from inventory page
		When user logs out from the application
		Then user should be redirected to the login page