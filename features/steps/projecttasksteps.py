import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

@when('I click on Project module')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[text() = 'Dự án']").click()


@when('I press "Create Project"')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//button[contains(@class, 'o-kanban-button-new')]").click()


@when('I enter the project name "project"')
def step_impl(context):
    context.driver.find_element(By.ID, "name").send_keys("project test")


@when('I click on the create project button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//button[@name='action_view_tasks']").click()
    time.sleep(1)


@then('Then new project should be created successfully')
def step_impl(context):
    breadcrumb = context.driver.find_element(By.XPATH, "//span[@class='text-truncate']")
    assert breadcrumb.text == "project test"


@when('I click on the firt project')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//div[@role='article'][1]").click()


@when('I click on the add stage button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//button[contains(text(),'Add a stage')]").click()


@then(u'I click on create task button')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I click on create task button')


@then(u'I enter the name task "task"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I enter the name task "task"')


@then(u'I click on the create task button')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I click on the create task button')


@then(u'Then new task should be created successfully')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Then new task should be created successfully')

    def div_datapoint(self):
        return self.driver.find_element(By.XPATH, "//div[@data-id='datapoint_109']")
