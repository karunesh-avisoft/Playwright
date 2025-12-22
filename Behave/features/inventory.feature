Feature: Inventory Management

	Background: User logged in and on inventory page
		Given User login as 'standard' user
		Then User navigates to the inventory page

	Scenario: Verify available products on inventory page
		Then User should see 6 products listed
	
	Scenario Outline: Sort products by different options
		When the user sorts products by '<sort_option>'
		Then the products should be sorted by '<sort_type>' order

		Examples:
			| sort_option             | sort_type        |
			| az                      | name ascending   |
			| za                      | name descending  |
			| lohi                    | price ascending  |
			| hilo                    | price descending |

	Scenario: Logout from inventory page
		When user logs out from the application
		Then user should be redirected to the login page