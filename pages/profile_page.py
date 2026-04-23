import allure

from pages.base_page import BasePage
from locators.profile_page_lct import ProfilePageLocators


class ProfilePage(BasePage):

    @allure.step('Кликнуть на кнопку "История заказов"')
    def click_orders_history_button(self):
        self.check_element_displayed(ProfilePageLocators.ORDER_HISTORY_BUTTON)
        self.click_on_element(ProfilePageLocators.ORDER_HISTORY_BUTTON)

    @allure.step('Кликнуть на кнопку "Выход"')
    def click_logout_button(self):
        self.check_element_displayed(ProfilePageLocators.LOGOUT_BUTTON)
        self.click_on_element(ProfilePageLocators.LOGOUT_BUTTON)

    def get_profile_url(self):
        self.check_element_displayed(ProfilePageLocators.PROFILE_BUTTON)
        return self.get_current_url()

    def get_orders_history_url(self):
        self.check_element_displayed(ProfilePageLocators.ENABLED_ORDERS_HISTORY_BUTTON)
        return self.get_current_url()