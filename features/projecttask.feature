Feature: project task

  Background: common steps
    Given I launch Chrome browser
    When I open OryzaErp homepage
    And I enter the username "admin" and password "admin"
    And I click on the login button
    And I click on Project module

  Scenario: create project
    And I press "Create Project"
    And I enter the project name "project"
    And I click on the create project button
    Then Then new project should be created successfully
    And I capture the screenshot

#  Scenario: create task
#    And I click on the firt project
#    And I click on the add stage button
#    And I click on create task button
#    And I enter the name task "task"
#    And I click on the create task button
#    Then Then new task should be created successfully
#    And I capture the screenshot