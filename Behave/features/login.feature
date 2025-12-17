Feature: User Login

  Scenario: Successful user login
     Given User on the login page
      When User enter 'standard' and password
      And User submit the login form
      Then User should be logged in successfully