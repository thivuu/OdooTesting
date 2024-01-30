from behave import *
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import os
import glob


@given('I launch Chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.implicitly_wait(1)


@when('I open OryzaErp homepage')
def step_impl(context):
    context.driver.get("https://erp3-test.oryza.vn/web/login")


@when('I enter the username "{user}" and password "{pwd}"')
def step_impl(context, user, pwd):
    context.driver.find_element(By.NAME, "login").send_keys(user)
    context.driver.find_element(By.NAME, "password").send_keys(pwd)


@when('I click on the login button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//button[@type='submit']").click()


@then('User must be successfully login to the Dashboard page')
def step_impl(context):
        homemenu = context.driver.find_element(By.XPATH, "//button[title='Home Menu']")
        assert homemenu.is_displayed()




