import pytest
from readconfig.read_config import ReadConfig
from selenium.webdriver import Chrome


@pytest.fixture()
def create_driver():
    driver_chrome = Chrome('chromedriver.exe')
    driver_chrome.maximize_window()
    driver_chrome.get(ReadConfig)
    yield driver_chrome
    driver_chrome.quit()
