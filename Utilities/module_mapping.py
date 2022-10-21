from Driver.selenium_driver import SeleniumDriver

class DriverMapping(SeleniumDriver):

    def __init__(self, driver):
        super(DriverMapping, self).__init__(driver)
        self.driver = driver

    def execute_keyword(self, keyword, attribute, value, object_name):
        if keyword == 'navigate':
            result = None
            result = self.navigate(value)
            return result
        if keyword == 'input':
            result = None
            result = self.sendKeys(value, object_name)
            return result
        # if keyword == 'click':
        #     result = None
        #     result = self.
