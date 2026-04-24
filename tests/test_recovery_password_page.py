import allure

from config import BASE_URL
from data.url import Url


class TestRecoveryPassword:

    @allure.title('Проверка перехода на страницу восстановления пароля по кнопке "Восстановить пароль"')
    def test_click_password_reset_button(self, pages):
        pages.click_login_account_button()
        pages.click_password_reset_link()
        current_url = pages.get_current_url()
        expected_result = BASE_URL + Url.FORGOT_PASS

        with allure.step('Cравнить текущий URL с ожидаемым /forgot-password'):
            assert current_url == expected_result

    @allure.title('Проверка ввода почты и перехода после клика по кнопке "Восстановить"')
    def test_enter_email_and_click_reset(self, pages):
        pages.go_to_forgot_password_page()
        pages.enter_email_for_reset_password()
        pages.click_reset_button()
        pages.find_save_button()
        current_url = pages.get_current_url()
        expected_result = BASE_URL + Url.RESET_PASS

        with allure.step('Cравнить текущий URL с ожидаемым /reset-password'):
            assert current_url == expected_result

    @allure.title('Проверка, что клик по кнопке Показать/скрыть пароль делает поле активным')
    def test_make_field_active(self, pages):
        pages.go_to_forgot_password_page()
        pages.enter_email_for_reset_password()
        pages.click_reset_button()
        pages.find_save_button()
        pages.click_on_show_password_button()
        assert pages.find_input_active()