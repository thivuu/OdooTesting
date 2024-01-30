Feature: OryzaErp Login
  Scenario: Login to the OryzaErp with valid parameters
    Given I launch Chrome browser
    When I open OryzaErp homepage
    And I enter the username "admin" and password "admin"
    And I click on the login button
    Then User must be successfully login to the Dashboard page
    And I capture the screenshot

Scenario Outline: Login to OryzaErp with Multiple parameters
    Given I launch Chrome browser
    When I open OryzaErp homepage
    And I enter the username "<username>" and password "<password>"
    And I click on the login button
    Then User must be successfully login to the Dashboard page
    And I capture the screenshot


    Examples:
      | username | password |
      | admin    | admin    |
      | Admin123 | admin123 |
      | Admin    | admin    |
      | Adminxyz | admiN1223 |
