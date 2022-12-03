import time

import pytest


@pytest.mark.smoke
def test_login(
        open_login_window):  # to pass this test please make break point in assert run in debug and by hands fill captcha
    """" function for auto login on Chrome browse"""
    login_window = open_login_window
    all_courses = login_window.login("test_auto50@gmail.com", 'number2000')
    assert all_courses.user_avatar_is_visible() is True, 'User not login'


@pytest.mark.regression
@pytest.mark.parametrize("password", ['number1800', '', 'фількіна грамота'])
def test_02_invalid_password_login(open_login_window, password): # to pass this test please make break point in assert run in debug and by hands fill captcha
    login = open_login_window
    login_window = login.login_with_invalid_password("test_auto50@gmail.com", password)
    assert login_window.is_alert_present() is True, "User enter valid password"

@pytest.mark.regression
@pytest.mark.parametrize("email", ['test_auto50@gmail.com', '', 'test_auto50@gmail'])
def test_02_invalid_password_login(open_login_window, email): # to pass this test please make break point in assert run in debug and by hands fill captcha
    login = open_login_window
    login_window = login.login_with_invalid_password(email, 'number2000')
    assert login_window.is_alert_present() is True, "User enter valid password"

@pytest.mark.regression
def test_register_user(open_register_window):
    register = open_register_window
    assert register.is_title_visible() is True, "Open Login window to provide registration"

@pytest.mark.smoke
def test_user_logaut(open_login_window, main_screen):
    login = open_login_window
    login_window = login.login_with_invalid_password('test_auto50@gmail.com', 'number2000')
    window = main_screen.click_drop_down().logaut()
    assert window.user_avatar_is_visible() is False, "User still logged"

@pytest.mark.regression
def test_login_with_remember_me(open_login_window, main_screen): #there is  a bug remember me not work
    login = open_login_window
    login_window = login.login_with_remember('test_auto50@gmail.com', 'number2000')
    window = main_screen.click_drop_down().logaut()
    email = open_login_window.click_sing_in_button()
    assert login_window.is_alert_present() is False, "user doesn't tick check box"


