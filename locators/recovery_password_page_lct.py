from selenium.webdriver.common.by import By


class RecoveryPasswordPageLocators:
    INPUT_EMAIL = (By.XPATH, './/label[text()="Email"]//parent::*/input[@type="text" and @name="name"]')
    PASSWORD_FIELD_ACTIVE = (By.CSS_SELECTOR, '.input.input_status_active')
    RESET_PASSWORD_BUTTON = (By.XPATH, '//button[text()="Восстановить"]')
    SAVE_BUTTON = (By.XPATH, '//button[text()="Сохранить"]')
    SHOW_PASSWORD_BUTTON = (By.XPATH, '//div[contains(@class,"icon-action")]')