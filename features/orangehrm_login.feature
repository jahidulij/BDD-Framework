Feature: OHRM OrangeHRM Login

  Scenario: OHRM Login to OrangeHRM with valid parameters
    Given OHRM I launch chrome browser
    When OHRM I open OrangeHRM homepage
    And OHRM enter username "admin" and password "admin123"
    And OHRM click on login button
    Then OHRM user must successfully login to the dashboard page

  Scenario Outline: OHRM Login to OrangeHRM with multiple parameters
    Given OHRM I launch chrome browser
    When OHRM I open OrangeHRM homepage
    And OHRM enter username "<username>" and password "<password>"
    And OHRM click on login button
    Then OHRM user must successfully login to the dashboard page

    Examples:
    | username | password |
    | admin    | admin123 |
    | Admin    | admin123 |
