from selenium.webdriver.common.by import By


class ProfilePageLocators:
    PROFILE_BUTTON = (By.LINK_TEXT, 'Профиль')
    ORDER_HISTORY_BUTTON = (By.LINK_TEXT, 'История заказов')
    ENABLED_ORDERS_HISTORY_BUTTON = (By.XPATH, '//ul/li[2]/a[contains(@class, "Account_link_active")]')
    LOGOUT_BUTTON = (By.XPATH, './/button[text()="Выход"]')