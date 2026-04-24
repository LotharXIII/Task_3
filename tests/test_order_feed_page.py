import allure
import pytest

from locators.order_feed_page_lct import OrderFeedPageLocators


class TestCreateOrder:
    @allure.title('Проверка отображения поп-апа с деталями при клике на заказ')
    def test_get_order_popup(self, pages):
        pages.click_order_feed_button()
        pages.click_order()

        structure_text = pages.get_text_order_structure()

        with allure.step('Cравнить текст в детализации заказа'):
            assert structure_text == "Cостав"

    @allure.title('Проверка отображения заказов пользователя из раздела "История заказов" на странице "Лента заказов"')
    def test_find_order_in_list(self, pages, created_order):
        order_id = created_order
        pages.click_profile_button()
        pages.click_orders_history_button()
        order_id_history = pages.order_id_found_in_history_orders(order_id)
        pages.click_order_feed_button()
        order_id_feed = pages.order_id_found_in_order_feed(order_id)

        with allure.step('Cравнить номер заказа из "Истории заказов" с заказом в "Ленте заказов"'):
            assert order_id_history == order_id_feed

    @pytest.mark.parametrize('name_counter, counter',
                             [['Выполнено за все время', OrderFeedPageLocators.TOTAL_ORDER_COUNT],
                              ['Выполнено за сегодня', OrderFeedPageLocators.DAILY_ORDER_COUNT]])
    def test_orders_counter(self, pages, login_user, name_counter, counter):
        allure.dynamic.title(f'Проверка увеличения счетчика "{name_counter}" при создании нового заказа')
        pages.click_order_feed_button()
        prev_counter_value = pages.get_total_order_count(counter)
        pages.click_constructor_button()
        pages.create_order()
        pages.click_order_feed_button()
        current_counter_value = pages.get_total_order_count(counter)

        with allure.step(f'Проверить, что счетчик "{name_counter}" увеличился'):
            assert current_counter_value > prev_counter_value

    @allure.title('Проверка отображения номера созданного заказа в разделе "В работе"')
    def test_new_order_display_in_progress(self, pages, created_order):
        order_id = created_order
        pages.click_order_feed_button()
        order_in_progress = pages.get_user_order_in_progress()

        with allure.step(
                f'Проверить, что номер созданного заказа совпадает с номером последнего заказа из раздела "В работе"'):
            assert order_id == order_in_progress