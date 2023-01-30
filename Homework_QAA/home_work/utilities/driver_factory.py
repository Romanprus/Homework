from selenium.webdriver import Chrome, Firefox, Edge, Safari
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.edge.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.safari.options import Options



class DriverFactory:
    CHROME = 1
    FIREFOX = 2
    EDGE = 3
    Safari = 4

    @staticmethod
    def create_driver(driver_id: int, is_headless=False):
        if int(driver_id) == DriverFactory.CHROME:
            chrome_options = Options()
            if is_headless:
                chrome_options.add_argument("--headless")
            driver = Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        elif int(driver_id) == DriverFactory.FIREFOX:
            driver = Firefox(service=Service(GeckoDriverManager().install()))
        elif int(driver_id) == DriverFactory.EDGE:
            driver = Edge(service=Service(EdgeChromiumDriverManager().install()))
        elif int(driver_id) == DriverFactory.Safari:
            safari_options = Options()
            if is_headless:
                safari_options.add_argument("--headless")
                safari_options.add_argument("--no-sandbox")
            driver = Safari()
        else:
            driver = Chrome(service=Service(ChromeDriverManager().install()))
        return driver
