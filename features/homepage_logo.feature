Feature: Swag Labs homepage logo

  Scenario: Logo presence on Swag Labs homepage
    Given launch chrome browser
    When open swag labs homepage
    Then verify that logo present in the homepage
    And close the browser
