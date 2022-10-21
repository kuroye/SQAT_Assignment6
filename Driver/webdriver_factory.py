from selenium import webdriver
import os
from Utilities.constant import Constant

class GetWebDriverInstance():

    def __init__(self, browser):
        self.browser = browser
        self.constant = Constant()

    def getBrowserInstance(self):
        if self.browser == 'IE':
            driver_location = self.constant.Path_IE_driver
            os.environ['webdriver.IE.driver'] = driver_location
            driver = webdriver.Ie(driver_location)
            driver.maximize_window()
            driver.implicitly_wait(5)
            driver.delete_all_cookies()
        elif self.browser == 'Chrome':

            driver_location = self.constant.Path_Chrome_driver
            os.environ['webdriver.chrome.driver'] = driver_location
            driver = webdriver.Chrome(driver_location)
            driver.maximize_window()
            driver.implicitly_wait(5)
            driver.delete_all_cookies()

        else:

            driver = webdriver.Firefox()
            driver.maximize_window()
            driver.implicitly_wait(5)
            driver.delete_all_cookies()

        return driver
