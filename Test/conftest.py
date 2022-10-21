import pytest
from Driver.webdriver_factory import GetWebDriverInstance

@pytest.yield_fixture(scope='class')
def invoke_browser(request, browser):
    wdf = GetWebDriverInstance(browser)
    driver = wdf.getBrowserInstance()

    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()

def pytest_add_option(parser):
    parser.add_option('--browser')

@pytest.fixture(scope='session')
def browser(request):
    return request.config.get_option('browser')
