import inspect
import logging


class CustomLogger():

    def log_utility(loglevel=logging.DEBUG):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        logger.setLevel(loglevel)

        lhandler = logging.FileHandler('run.html', 'a')
        lhandler.setLevel(loglevel)

        formatter = logging.Formatter('%(name)s: %(asctime)s: %(levelname)s: %(message)s\n\r',
                                      datefmt='%m/%d/%Y %I:%M:%S %p')

        lhandler.setFormatter(formatter)

        logger.addHandler(lhandler)

        return logger
