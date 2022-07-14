Feature: Swag Labs Login

  Scenario: Login to Swag Labs with valid parameters
    Given I launch chrome browser
    When I open swag labs homepage
    And enter username "standard_user" and password "secret_sauce"
    And click on login button
    Then user must successfully login to the dashboard page
