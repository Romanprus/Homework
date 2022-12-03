from selenium.webdriver.common.by import By


from Homework_QAA.home_work.utilities.web_ui.base_page import BasePage


class ResetPage(BasePage):
    def __init__(self, driver):
        self._driver = driver
        super().__init__(driver)

    __success_reset_screen = (By.XPATH, "//*[text()='Help is on the way!']")
    __sign_in = (By.XPATH, "//div[@class='header__wrapper']//a[@href='/users/sign_in']")
    __enter_button = (By.XPATH, "//div//div//input[@value='Sign in']")

    def sucssess_title(self):
        return self._is_displayed(self.__success_reset_screen)

    def back_to_sign_in_screen(self):
        self._click(self.__sign_in)
        return self

    def is_sign_in_button_displayed(self):
        return self._is_displayed(self.__enter_button)