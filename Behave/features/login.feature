Feature: User Login

	Scenario: Successful user login
		Given User on the login page
		When User enters 'standard' as username
		And User submit the login form
		Then User navigates to the inventory page
	
	@invalid_login
	Scenario: Unsuccessful user login with incorrect username
		Given User on the login page
		When User enters 'wrongUser' as username
		And User submit the login form
		Then User should see an error message indicating incorrect/incomplete credentials