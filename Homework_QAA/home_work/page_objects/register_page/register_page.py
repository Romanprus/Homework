from selenium.webdriver.common.by import By
from Homework_QAA.home_work.utilities.web_ui.base_page import BasePage


class RegisterPage(BasePage):
    def __init__(self, driver):
        self._driver = driver
        super().__init__(driver)

    __title = (By.XPATH, '//article[@class="sign-up__form"]//h1[@class="page__heading" and text()]')
    __first_name = (By.XPATH, "//label//input[@id='user[first_name]']")
    __last_name = (By.XPATH, '//input[@id="user[last_name]"]')
    __email = (By.XPATH, '//input[@id="user[email]"]')
    __password = (By.XPATH, '//input[@id="user[password]"]')
    __terms_check_box = (By.CSS_SELECTOR, 'label input[id="user[terms]"]')
    __terms_link = (By.XPATH, "//label//a[text()='Terms of Use']")
    __sign_up_button = (By.CSS_SELECTOR, 'div[class="form__button-group"] input')
    __have_acc_link = (By.XPATH, "//aside//a[text()]")
    __sign_in_link = (By.CSS_SELECTOR, "section ul:last-child li:last-child a")
    __user_avatar = (By.XPATH, "//img[@class='header__user-avatar']")
    __terms_page = (By.XPATH, "//[text()='ULTIMATEQA.COM’S']")
    __error_list = (By.CSS_SELECTOR, 'ul[class="form-error__list"]')

    def is_title_visible(self):
        return self._is_displayed(self.__title)

    def set_first_name(self, name):
        return self._send_keys(self.__first_name, name)

    def set_last_name(self, last_name):
        return self._send_keys(self.__last_name, last_name)

    def set_email(self, email):
        return self._send_keys(self.__email, email)

    def set_password(self, password):
        return self._send_keys(self.__password, password)

    def tick_terms_checkbox(self):
        self._tick(self.__terms_check_box)
        return self

    def click_sign_up_button(self):
        self._click(self.__sign_up_button)
        return self

    def create_new_user(self, name, last_name, email, password):
        self.set_first_name(name)
        self.set_last_name(last_name)
        self.set_email(email)
        self.set_password(password)
        self.tick_terms_checkbox().click_sign_up_button()
        return self

    def open_terms_page(self):
        self._click(self.__terms_link)
        return self

    def user_avatar_is_visible(self):
        return self._is_displayed(self.__user_avatar)

    def error_list(self):
        return self._is_displayed(self.__error_list)

    def have_account(self):
        self._click(self.__have_acc_link)
        return self
