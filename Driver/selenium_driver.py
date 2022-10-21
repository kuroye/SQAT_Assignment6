from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from Utilities.custom_logger import CustomLogger as lg
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from Utilities.constant import Constant

import time
import logging

class SeleniumDriver():

    log = lg.log_utility(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver
        self.constant = Constant()

    def navigate(self, data_value):
        try:
            self.driver.get(data_value)
            return True
        except:
            self.log.error('Navigation failed')
            return False

    def get_element(self, locator):
        try:
            element = self.driver.find_element(By.XPATH, locator)
        except:
            self.log.info('Element not found')

        return element

    def find_element(self, locator):
        try:

            element_to_find = None
            element_to_find = self.driver.find_elements(By.XPATH,locator)

            if len(element_to_find)>0:
                return True
            else:
                self.log.info('Element not found')
                return False
        except:
            self.log.info('Some error occurred, element not found')
            return False

    def element_click(self, locator):
        try:
            self.get_element(locator).click()
            return True
        except:
            self.log.info('Element not clicked')
            return False

    def send_keys(self, data, locator):
        try:
            self.get_element(locator).clear()
            self.get_element(locator).send_keys(data)
            return True
        except:
            self.log.info('Cannot send data to the element')
            return False

    def capture_screen(self):
        try:
            filename = 'Screenshot'+'_'+str(round(time.time()*1000))+'.png'
            folder_location = self.constant.Path_SnapShot
            destination = folder_location+filename
            self.driver.save_screenshot(destination)
            return True
        except NotADirectoryError:
            self.log.info('Capture screenshot failed')
            return False

    def get_title(self):
        return self.driver.title

