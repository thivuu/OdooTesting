import os
import shutil
import time

from behave import *
from selenium.webdriver.common.by import By
from faker import Faker

faker = Faker()


@when('I click on CRM module')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[text() = 'CRM']").click()


@when('I click on Create button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//button[@title='Bán hàng']").click()
    context.driver.find_element(By.XPATH, "//a[contains(text(),'Khách hàng')]").click()
    time.sleep(1)


@when('I enter the customer name')
def step_impl(context):
    context.driver.find_element(By.ID, "name").send_keys("customer test")


@when('I click on avatar button and select the image from folder "{folder_path}"')
def step_impl(context, folder_path):
    def random_name():
        return faker.name()

    for filename in os.listdir(folder_path):

        try:
            if filename.endswith((".jpg", ".png", ".jpeg")):
                context.driver.find_element(By.XPATH, "//button[@accesskey='c']").click()
                time.sleep(3)

                context.driver.find_element(By.XPATH, "//*[@id='name_1']").send_keys(random_name())
                cloud_button = context.driver.find_element(By.XPATH, "//button[@data-hotkey='s']")
                time.sleep(3)

                avatar_input = context.driver.find_element(By.XPATH, "//input[@type='file']")
                image_path = os.path.join(folder_path, filename)

                avatar_input.send_keys(image_path)
                time.sleep(3)
                cloud_button.click()
                time.sleep(15)

                context.driver.find_element(By.XPATH, "//li[@data-hotkey='b']").click()
        except Exception as e:
            print(e)
            failed_folder = os.path.join(folder_path, "test failed")
            os.makedirs(failed_folder, exist_ok=True)
            shutil.move(os.path.join(folder_path, filename), os.path.join(failed_folder, filename))
            context.driver.find_element(By.XPATH, "//button[@class='btn btn-primary o-default-button']").click()
            time.sleep(3)
            context.driver.find_element(By.XPATH, "//button[@data-hotkey='j']").click()
            time.sleep(1)
            context.driver.find_element(By.XPATH, "//li[@data-hotkey='b']").click()

            continue


