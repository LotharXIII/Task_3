from selenium.webdriver.common.by import By


class AuthPageLocators:
    EMAIL_FIELD = (By.XPATH, './/label[text()="Email"]//parent::*/input[@type="text" and @name="name"]')
    PASSWORD_FIELD = (By.XPATH, './/input[@type="password" and @name="Пароль"]')
    LOGIN_BUTTON = (By.XPATH, './/button[text()="Войти"]')
    FORGOT_PASSWORD = (By.XPATH, '//a[contains(@href, "/forgot-password")]')