Feature: Add customer to CRM

  Background: common steps
    Given I launch Chrome browser
    When I open OryzaErp homepage
    And I enter the username "admin" and password "admin"
    And I click on the login button
    And I click on CRM module

  Scenario: Add customer to CRM
    When I click on Create button
#    And I enter the customer name "Name"
    And I click on avatar button and select the image from folder "C:\Users\Oryza-JSC\Downloads\lfw\lfw\collect"
#    And I click on cloud button
#    Then I should see the customer added successfully
     And I capture the screenshot

#  Scenario Outline: Add customer to CRM with multiple images path
#    When I click on Create button
##    And I enter the customer name "<Name>"
#    And I click on avatar button and select the image from folder "<path>"
##    Then I should see the customer added successfully
#    And I capture the screenshot
#
#
#    Examples:
#      | path |
#      | C:\Users\Oryza-JSC\Downloads\archive\105_classes_pins_dataset\pins_elon musk|
#      |C:\Users\Oryza-JSC\Downloads\archive\105_classes_pins_dataset\pins_ellen page|
#      | C:\Users\Oryza-JSC\Downloads\archive\105_classes_pins_dataset\pins_margot robbie|
#      | C:\Users\Oryza-JSC\Downloads\archive\105_classes_pins_dataset\pins_elizabeth olsen|
#      | C:\Users\Oryza-JSC\Downloads\archive\105_classes_pins_dataset\pins_camila mendes|
#      | C:\Users\Oryza-JSC\Downloads\archive\105_classes_pins_dataset\pins_barbara palvin|
#      |C:\Users\Oryza-JSC\Downloads\archive\105_classes_pins_dataset\pins_barack obama|
