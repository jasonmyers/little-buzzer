Feature: Confirming that a webpage displays

	 Scenario: Check that the main page displays
	 	   When I go to the front page of the site
		   Then I should see that the title is "Little Buzzer"

	 Scenario: Check that a user can log in
	 	   When I go to the front page of the site
		   And I submit my username and password
		   Then I should see welcome text

	 Scenario: Check that a user can log out
	 	   When I go to the front page of the site
		   And I click the logout button
		   Then I should see a request to log in again