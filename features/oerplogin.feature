Feature: OrangeHRM LOgin
  Scenario: Login to the OrangeHRM with valid parameters
    Given I launch Chrome browser
    When I open OrangeHRM homepage
    And I enter the username "admin" and password "admin"
    And I click on the login button
    Then User must be successfully login to the Dashboard page
    And I capture the screenshot

Scenario Outline: Login to OrangeHRM with Multiple parameters
    Given I launch Chrome browser
    When I open OrangeHRM homepage
    And I enter the username "<username>" and password "<password>"
    And I click on the login button
    Then User must be successfully login to the Dashboard page
    And I capture the screenshot


    Examples:
      | username | password |
      | admin    | admin    |
      | Admin123 | admin123 |
      | Admin    | admin    |
      | Adminxyz | admiN123 |