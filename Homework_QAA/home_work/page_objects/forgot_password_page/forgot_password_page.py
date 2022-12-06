from selenium.webdriver.common.by import By

from Homework_QAA.home_work.page_objects.forgot_password_page.reset_page import ResetPage
from Homework_QAA.home_work.utilities.web_ui.base_page import BasePage


class ForgotPass(BasePage):
    def __init__(self, driver):
        self._driver = driver
        super().__init__(driver)

    __screen_title = (By.XPATH, "//div[@class='password-reset__wrapper']//h2")
    __email_field = (By.XPATH, "//input[@id='user[email]']")
    __submit_button = (By.XPATH, '//input[@value="Submit"]')
    __enter_button = (By.XPATH, "//div//div//input[@value='Sign in']")
    __sign_in = (By.XPATH, "//div[@class='header__wrapper']//a[@href='/users/sign_in']")

    def is_title_present(self) -> 'bool':
        return self._is_displayed(self.__screen_title)

    def title_value(self):
        element = self._get_value(self.__screen_title)
        return element

    def is_email_field_present(self) -> 'bool':
        return self._is_displayed(self.__email_field)

    def set_email(self, email):
        self._send_keys(self.__email_field, email)
        return self

    def click_submit(self):
        self._click(self.__submit_button)
        return self

    def reset_password(self, email):
        self.set_email(email)
        self.click_submit()
        return ResetPage(self._driver)

    def reset_pass_with_empty_mail(self):
        self.set_email('')
        self.click_submit()
        return ForgotPass(self._driver)

    def back_to_signin_after_reset_pass(self, email):
        self.set_email(email)
        self.click_submit()
        return ResetPage(self._driver)

    def is_sign_in_button_displayed(self) -> 'bool':
        return self._is_displayed(self.__enter_button)

    def back_to_sign_in_screen(self):
        self._click(self.__sign_in)
        return self
