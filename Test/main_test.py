from Utilities.test_status import TestStatus
import unittest
import pytest
from ddt import ddt, data, unpack
from Utilities.constant import Constant
from Utilities.excel_read import ExcelUnit
from Utilities.module_mapping import DriverMapping
from Utilities.custom_logger import CustomLogger as lg
import logging

@pytest.mark.usefixtures('invoke_browser')
@ddt
class MainTest(unittest.TestCase):

    log = lg.log_utility(logging.INFO)
    # Initialize object instance for test case result, constants, excel data, method mapping
    @pytest.fixture(autouse=True)
    def initial_setup(self, invoke_browser):
        self.ts = TestStatus(self.driver)
        self.constants = Constant()
        self.excel = ExcelUnit()
        self.driver_method = DriverMapping(self.driver)

    @pytest.mark.run(order=1)
    def test_main(self):
        self.excel.set_excel_file(self.constants.Path_TestData)
        self.execute_test_cases()

    def execute_test_cases(self):
        n_total_test_cases = self.excel.get_row_count(self.constants.Sheet_TestCase)


