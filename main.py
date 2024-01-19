# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

    def input_user_name(self):
        return self.driver.find_element(By.XPATH, "//*[@id='userName-id']")


    def input_user_name(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#userName-id")


    def input_user_name(self):
        return self.driver.find_element(By.NAME, "userName")


    def input_user_name(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#userName-id")


    def input_user_name(self):
        return self.driver.find_element(By.CSS_SELECTOR, "input[id='userName-id']")


    def fieldset_outlined_notched(self):
        return self.driver.find_element(By.CSS_SELECTOR,
                                        "html > body > div > div:nth-of-type(2) > main > div > div > form > div:nth-of-type(1) > div > div > div > div > fieldset")
