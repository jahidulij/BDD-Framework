Feature: OrangeHRM Login

  Background: Common steps
    Given HRM Launch chrome browser
    When HRM Open OrangeHRM application
    And HRM Enter valid username and password
    And HRM Click on login

  Scenario: Login to OrangeHRM
    Then HRM User must successfully login to the dashboard page

  Scenario: Search user
    When HRM navigate to search page
    Then HRM search page should display

  Scenario: Advanced search user
    When HRM navigate to advanced search page
    Then HRM advanced search page should display