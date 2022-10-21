import xlrd
from Utilities.custom_logger import CustomLogger as lg
from Utilities.constant import Constant
import logging

class ExcelUnit():

    log = lg.log_utility(logging.DEBUG)
    constant = Constant()

    def set_excel_file(self,path):
        try:
            self.workbook = xlrd.open_workbook(path)
        except:
            self.log.error('Data file was not opened')