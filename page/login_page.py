import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
class LoginPage:

    def __init__(self,driver):
        self.driver=driver
        self.__un=(By.NAME,"username")
        self.__pw=(By.NAME,"password")
        self.__go=(By.NAME,"login-button")

    def set_username(self,un):
        self.driver.find_element(*self.__un).send_keys(un)

    def set_password(self,pw):
        self.driver.find_element(*self.__pw).send_keys(pw)

    def click_go(self):
        self.driver.find_element(*self.__go).click()

