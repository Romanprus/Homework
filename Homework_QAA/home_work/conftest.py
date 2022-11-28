import pytest
from Homework_QAA.home_work.utilities.driver_factory import DriverFactory
from Homework_QAA.home_work.utilities.read_configs import ReadConfig
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope='session')
def create_driver():
    driver = DriverFactory.create_driver(driver_id=ReadConfig.get_driver_id())
    driver.maximize_window()
    driver.get(ReadConfig.get_base_url())
    yield driver
    driver.quit()


@pytest.fixture()
def create_wait(create_driver):
    wait = WebDriverWait(create_driver, 5)
