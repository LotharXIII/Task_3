import allure

from config import BASE_URL
from data.url import Url


class TestProfile:
    @allure.title('Проверка перехода в ЛК по клику на кнопку "Личный кабинет"')
    def test_go_to_account_from_header(self, pages, login_user):
        pages.click_profile_button()
        current_url = pages.get_profile_url()
        expected_result = BASE_URL + Url.PROFILE

        with allure.step('Cравнить текущий URL с ожидаемым /account/profile'):
            assert current_url == expected_result

    @allure.title('Проверка перехода в ЛК в раздел История заказов по кнопке "История заказов"')
    def test_go_to_order_history(self, pages, login_user):
        pages.click_profile_button()
        pages.click_orders_history_button()
        current_url = pages.get_orders_history_url()
        expected_result = BASE_URL + Url.ORDERS_HISTORY

        with allure.step('Cравнить текущий URL с ожидаемым /account/order-history'):
            assert current_url == expected_result

    @allure.title('Проверка перехода на страницу авторизации при нажатии в ЛК кнопки "Выход"')
    def test_logout(self, pages, login_user):
        pages.click_profile_button()
        pages.click_logout_button()
        current_url = pages.get_login_url()
        expected_result = BASE_URL + Url.LOGIN

        with allure.step('Cравнить текущий URL с ожидаемым /login'):
            assert current_url == expected_result