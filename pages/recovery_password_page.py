import allure

from pages.base_page import BasePage
from locators.recovery_password_page_lct import RecoveryPasswordPageLocators
from locators.auth_page_lct import AuthPageLocators
from data.url import Url
from data.user_data import UserData


class RecoveryPasswordPage(BasePage):

    @allure.step('Перейти на страницу /forgot-password')
    def go_to_forgot_password_page(self):
        self.open_page(Url.FORGOT_PASS)

    @allure.step('Кликнуть по ссылке "Восстановить пароль"')
    def click_password_reset_link(self):
        self.click_on_element(AuthPageLocators.FORGOT_PASSWORD)

    @allure.step('Ввести email в поле для восстановления пароля')
    def enter_email_for_reset_password(self):
        self.input_text(RecoveryPasswordPageLocators.INPUT_EMAIL, UserData.EMAIL)

    @allure.step('Нажать кнопку "Восстановить"')
    def click_reset_button(self):
        self.check_element_displayed(RecoveryPasswordPageLocators.RESET_PASSWORD_BUTTON)
        self.click_on_element(RecoveryPasswordPageLocators.RESET_PASSWORD_BUTTON)

    @allure.step('Кликнуть на кнопку Показать/скрыть пароль')
    def click_on_show_password_button(self):
        self.check_element_displayed(RecoveryPasswordPageLocators.SHOW_PASSWORD_BUTTON)
        self.click_on_element(RecoveryPasswordPageLocators.SHOW_PASSWORD_BUTTON)

    def find_save_button(self):
        self.check_element_displayed(RecoveryPasswordPageLocators.SAVE_BUTTON)

    @allure.step('Найти активное поле "Пароль"')
    def find_input_active(self):
        return self.check_element_displayed(RecoveryPasswordPageLocators.PASSWORD_FIELD_ACTIVE)