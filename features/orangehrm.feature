Feature: OH OrangeHRM Logo

  Scenario: OH Logo presence on OrangeHRM homepage
    Given OH launch chrome browser
    When OH open OrangeHRM homepage
    Then OH verify that logo present in the homepage
    And OH close the browser
