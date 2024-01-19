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
    context.driver.implicitly_wait(10)


@when('I open OrangeHRM homepage')
def step_impl(context):
    context.driver.get("https://erp5-test.oryza.vn/web/login")


@when('I enter the username "{user}" and password "{pwd}"')
def step_impl(context,user,pwd):
    context.driver.find_element(By.NAME, "login").send_keys(user)
    context.driver.find_element(By.NAME, "password").send_keys(pwd)


@when('I click on the login button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//button[@type='submit']").click()

@then('User must be successfully login to the Dashboard page')
def step_impl(context):
    try:
        homemenu = context.driver.find_element(By.XPATH, "//button[title='Home Menu']")
        if homemenu.is_displayed():
            print("Test Passed")
        else:
            print("Test Failed")
    except NoSuchElementException:
        print("Test Failed")

# @then('I capture the screenshot')
# def step_impl(context):
#     # Create the capture directory if it doesn't exist
#     capture_dir = os.path.join(os.path.dirname(__file__), '..', 'capture')
#     os.makedirs(capture_dir, exist_ok=True)
#
#     # Delete all existing screenshots
#     screenshot_files = glob.glob(os.path.join(capture_dir, 'screenshot_*.png'))
#     for file in screenshot_files:
#         os.remove(file)
#
#     # Capture the screenshot and save it to the capture directory
#     feature_name = context.feature.name.replace(" ", "_")
#     screenshot_path = os.path.join(capture_dir, f'{feature_name}_{context.scenario.name}_screenshot.png')
#     context.driver.save_screenshot(screenshot_path)
#
#     context.driver.close()

