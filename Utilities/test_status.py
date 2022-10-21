from Utilities.custom_logger import CustomLogger as lg
import logging
from Driver.selenium_driver import SeleniumDriver


class TestStatus(SeleniumDriver):
    log = lg.log_utility(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.result_list = []

    def set_result(self, result, result_message):
        if result in None:
            self.result_list.append('Fail')
            self.log.info(str(result_message) + ':Fail')
            self.capture_screen()
        else:
            if result:
                self.result_list.append('Pass')
                self.log.info(str(result_message) + ':Pass')
            else:
                self.result_list.append('Fail')
                self.log.info(str(result_message) + ':Fail')
                self.capture_screen()

    def mark(self, result, result_message):
        self.set_result(result, result_message)

    def mark_final(self, test_name, result, result_message):

        if 'Fail' in self.result_list:
            self.log.error('TestCase Failed' + test_name + ' :' + result_message)
            self.result_list.clear()
            assert False == False
        else:
            self.log.error('TestCase Passed' + test_name + ' :' + result_message)
            self.result_list.clear()
            assert True == True
