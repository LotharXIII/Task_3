import allure

from pages.base_page import BasePage
from locators.auth_page_lct import AuthPageLocators
from locators.main_page_lct import MainPageLocators


class AuthPage(BasePage):
    @allure.step('Кликнуть на кнопку "Войти в аккаунт"')
    def click_login_account_button(self):
        self.check_element_displayed(MainPageLocators.LOGIN_PROFILE_BUTTON)
        self.click_on_element(MainPageLocators.LOGIN_PROFILE_BUTTON)

    @allure.step('Заполнить поле "Email"')
    def input_email_field(self, email):
        self.check_element_displayed(AuthPageLocators.EMAIL_FIELD)
        self.click_on_element(AuthPageLocators.EMAIL_FIELD)
        self.input_text(AuthPageLocators.EMAIL_FIELD, email)

    @allure.step('Заполнить поле "Пароль"')
    def set_password_field(self, password):
        self.check_element_displayed(AuthPageLocators.PASSWORD_FIELD)
        self.click_on_element(AuthPageLocators.PASSWORD_FIELD)
        self.input_text(AuthPageLocators.PASSWORD_FIELD, password)

    @allure.step('Нажать кнопку "Войти"')
    def click_login_button(self):
        self.click_on_element(AuthPageLocators.LOGIN_BUTTON)

    def login(self, email, password):
        self.click_login_account_button()
        self.input_email_field(email)
        self.set_password_field(password)
        self.click_login_button()
        self.check_element_displayed(MainPageLocators.CONFIRM_ORDER_BUTTON)

    def get_login_url(self):
        self.check_element_displayed(AuthPageLocators.LOGIN_BUTTON)
        return self.get_current_url()