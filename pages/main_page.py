import allure

from pages.base_page import BasePage
from locators.main_page_lct import MainPageLocators


class MainPage(BasePage):

    @allure.step('Кликнуть на кнопку "Войти в аккаунт"')
    def click_login_account_button(self):
        self.check_element_displayed(MainPageLocators.LOGIN_PROFILE_BUTTON)
        self.click_on_element(MainPageLocators.LOGIN_PROFILE_BUTTON)

    @allure.step('Кликнуть на кнопку "Личный кабинет"')
    def click_profile_button(self):
        self.check_element_displayed(MainPageLocators.PROFILE_BUTTON)
        self.click_on_element(MainPageLocators.PROFILE_BUTTON)

    @allure.step('Кликнуть на кнопку "Конструктор"')
    def click_constructor_button(self):
        self.click_on_element(MainPageLocators.CONSTRUCTOR_BUTTON)
        self.check_element_displayed(MainPageLocators.CREATE_BURGER_TITLE)

    @allure.step('Кликнуть на кнопку "Лента заказов"')
    def click_order_feed_button(self):
        self.click_on_element(MainPageLocators.ORDER_FEED_BUTTON)
        self.check_element_displayed(MainPageLocators.ORDER_FEED_BUTTON)

    @allure.step('Кликнуть на первый ингредиент в списке')
    def click_on_first_ingredient(self):
        self.check_element_displayed(MainPageLocators.FIRST_INGREDIENT)
        self.click_on_element(MainPageLocators.FIRST_INGREDIENT)

    def title_popup_with_details(self):
        self.check_element_displayed(MainPageLocators.INGREDIENT_DETAILS_POPUP)
        return self.get_element_text(MainPageLocators.INGREDIENT_DETAILS_POPUP)

    @allure.step('Кликнуть на крестик закрытия поп-апа с ингредиентами')
    def click_on_popup_close_button(self):
        self.check_element_displayed(MainPageLocators.CLOSE_POPUP_DETAILS)
        self.click_on_element(MainPageLocators.CLOSE_POPUP_DETAILS)

    def invisibility_popup_with_details(self):
        return self.check_element_not_displayed(MainPageLocators.INGREDIENT_DETAILS_POPUP)

    def check_displayed_popup_with_details(self):
        return self.check_presence_element(MainPageLocators.INGREDIENT_DETAILS_POPUP).is_displayed()

    @allure.step('Получить значение каунтера ингредиента')
    def get_counter_value(self):
        return self.get_element_text(MainPageLocators.INGREDIENT_COUNTER)

    @allure.step('Добавить ингредиент в заказ')
    def add_ingredient_to_order(self):
        self.element_is_clickable(MainPageLocators.FIRST_INGREDIENT)
        self.drag_and_drop_on_element(MainPageLocators.FIRST_INGREDIENT, MainPageLocators.ORDER_BASKET)

    @allure.step('Кликнуть на кнопку "Оформить заказ"')
    def click_confirm_button(self):
        self.click_on_element(MainPageLocators.CONFIRM_ORDER_BUTTON)

    @allure.step('Получить номер заказа')
    def get_order_id(self):
        self.check_element_displayed(MainPageLocators.ORDER_ID)
        self.wait.until(
            lambda _: self.get_element_text(MainPageLocators.ORDER_ID) != '9999'
        )
        return self.get_element_text(MainPageLocators.ORDER_ID)

    @allure.step('Закрыть попап создания заказа')
    def click_close_popup_order(self):
        self.element_is_clickable(MainPageLocators.CLOSE_POPUP_ORDER)
        self.click_on_element(MainPageLocators.CLOSE_POPUP_ORDER)

    @allure.step('Создать заказ')
    def create_order(self):
        self.add_ingredient_to_order()
        self.click_confirm_button()
        order_id = self.get_order_id()
        self.click_close_popup_order()
        return order_id