import pytest
import allure

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FO


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help='Choose browser: chrome or firefox')


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption('browser_name')
    if browser_name == 'chrome':
        chrome_options = Options()
        browser = webdriver.Remote(
            command_executor='http://192.168.1.69:4444/wd/hub',
            options=chrome_options
        )
    elif browser_name == 'firefox':
        firefox_options = FO()
        browser = webdriver.Remote(
            command_executor='http://192.168.1.69:4444/wd/hub',
            options=firefox_options
        )
    else:
        raise pytest.UsageError('--browser_name should be chrome or firefox')
    yield browser
    browser.quit()


@pytest.fixture
def fixture_with_attachment_in_finalizer(request):
    def finalizer():
        allure.attach.file('transactions.csv')
    request.addfinalizer(finalizer)
