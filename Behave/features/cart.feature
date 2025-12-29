Feature: Cart Management

    Background: User logged in as standard user and on inventory page
        Given User login as 'standard' user
        Then User navigates to the inventory page

    @regression
    Scenario: Verify cart updates after adding items
		When User adds item 'bolt t-shirt' to the cart
		Then The cart badge should show the correct number of items

    @smoke
	Scenario: Verify cart updates after removing items
		When User adds item 'bolt t-shirt' to the cart
		And User adds item 'fleece jacket' to the cart
		And User removes item 'bolt t-shirt' from the cart
		Then The cart badge should show the correct number of items

    @regression
    Scenario: Verify items and navigation to checkout page from cart
        When User adds item 'fleece jacket' to the cart
		And User adds item 'bolt t-shirt' to the cart
        And User clicks on the cart icon
        Then User verify the items in cart
        When User proceeds to checkout page
        Then User should be navigated to the checkout page