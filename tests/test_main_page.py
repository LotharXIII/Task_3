import allure

from config import BASE_URL
from data.url import Url


class TestMainPage:

    @allure.title('Проверка перехода по клику на "Конструктор"')
    def test_go_to_constructor(self, pages):
        pages.click_order_feed_button()
        pages.click_constructor_button()
        current_url = pages.get_current_url()
        expected_result = BASE_URL + '/'

        with allure.step('Cравнить текущий URL с ожидаемым URL Главной страницы'):
            assert current_url == expected_result

    @allure.title('Проверка перехода по клику на "Лента заказов"')
    def test_go_to_order_feed(self, pages):
        pages.click_order_feed_button()
        current_url = pages.get_current_url()
        expected_result = BASE_URL + Url.FEED

        with allure.step('Cравнить текущий URL с ожидаемым /feed'):
            assert current_url == expected_result

    @allure.title('Проверка отображения поп-апа с деталями при клике на ингредиент')
    def test_open_popup_details_ingredient(self, pages):
        pages.click_on_first_ingredient()
        popup_title = pages.title_popup_with_details()

        with allure.step('Cравнить заголовок поп-апа с ожидаемым "Детали ингредиента"'):
            assert popup_title == "Детали ингредиента"

    @allure.title('Проверка закрытия поп-апа с деталями кликом по крестику')
    def test_close_popup_details_ingredient(self, pages):
        pages.click_on_first_ingredient()
        pages.click_on_popup_close_button()
        pages.invisibility_popup_with_details()

        with allure.step('Проверить, что поп-ап с деталями не отображается'):
            assert pages.check_displayed_popup_with_details() is False

    @allure.title('Проверка увеличения каунтера ингредиента при добавлении этого ингредиента в заказ')
    def test_ingredient_counter(self, pages):
        prev_counter_value = pages.get_counter_value()
        pages.add_ingredient_to_order()
        current_counter_value = pages.get_counter_value()

        with allure.step('Проверить, что каунтер у ингредиента увеличился'):
            assert current_counter_value > prev_counter_value

    @allure.title('Проверка возможности оформления заказа авторизованным пользователем')
    def test_successful_order(self, pages, login_user):
        pages.add_ingredient_to_order()
        pages.click_confirm_button()
        order_id = pages.get_order_id()

        with allure.step('Проверить, что номер заказа > 0'):
            assert int(order_id) > 0