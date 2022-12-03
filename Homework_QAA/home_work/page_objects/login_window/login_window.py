from selenium.webdriver.common.by import By

from Homework_QAA.home_work.page_objects.all_courses_page.all_courses_page import AllCourses
from Homework_QAA.home_work.page_objects.forgot_password_page.forgot_password_page import ForgotPass
from Homework_QAA.home_work.page_objects.register_page.register_page import RegisterPage
from Homework_QAA.home_work.utilities.web_ui.base_page import BasePage


class LoginWindow(BasePage):
    def __init__(self, driver):
        self._driver = driver
        super().__init__(driver)

    __sign_in = (By.XPATH, "//div[@class='header__wrapper']//a[@href='/users/sign_in']")
    __email_field = (By.XPATH, "//input[@id='user[email]']")
    __password_field = (By.CSS_SELECTOR, 'div input[type="password"]')
    __enter_button = (By.XPATH, "//div//div//input[@value='Sign in']")
    __check_box_remember = (By.XPATH, "//label//input[@id='user[remember_me]']")
    __create_account = (By.CSS_SELECTOR, "aside a")
    __forgot_pass = (By.XPATH, "//a[@class='form__forgot-password']")
    __facebook_login = (By.CSS_SELECTOR, "ul li a[class='button facebook']")
    __link_to_all_courses = (By.XPATH, "//section[@class='header__logo header__logo___2909e']//img")
    __message = (By.XPATH, "//*[text()='Welcome Back!']")
    __footer_link = (By.XPATH, "//*[text()='Powered By Thinkific']")
    __alert_message = (By.XPATH, "//li[text()='Invalid email or password.']")

    def click_on_sing_in(self):
        self._click(self.__sign_in)
        return self

    def set_email(self, email):
        self._send_keys(self.__email_field, email)
        return self

    def set_pass(self, password):
        self._send_keys(self.__password_field, password)
        return self

    def click_sing_in_button(self):
        return self._click(self.__enter_button)

    def login(self, email, password):
        self.click_on_sing_in().set_email(email).set_pass(password).click_sing_in_button()
        return AllCourses(self._driver)

    def click_create_new_acc(self):
        self._click(self.__create_account)
        return RegisterPage(self._driver)

    def tick_remember_me(self):
        return self._click(self.__check_box_remember)

    def login_with_remember(self, email, password):
        self.click_on_sing_in().set_email(email).set_pass(password).tick_remember_me()
        self.click_sing_in_button()
        return AllCourses(self._driver)

    def click_on_forgot_link(self):
        self._click(self.__forgot_pass)
        return ForgotPass(self._driver)

    def click_on_facebook_link(self):
        return self._click(self.__facebook_login)

    def login_without_data(self):
        return self.click_on_sing_in().click_sing_in_button()

    def login_with_invalid_password(self,email, password):
        self.click_on_sing_in().set_email(email).set_pass(password).click_sing_in_button()
        return LoginWindow(self._driver)

    def login_with_invalid_email(self, email, password):
        self.click_on_sing_in().set_email(email).set_pass(password).click_sing_in_button()
        return LoginWindow(self._driver)

    def is_alert_present(self):
        return self._is_displayed(self.__alert_message)

    def is_sign_in_button_displayed(self):
        return self._is_displayed(self.__enter_button)