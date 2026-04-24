from selenium.webdriver.common.by import By


class OrderFeedPageLocators:
    ORDER = (By.XPATH, '//*[contains(@class, "OrderHistory_link")]')
    ORDER_STRUCTURE = (By.XPATH, '//p[text()="Cостав"]')
    HISTORY_ORDERS = (By.XPATH,
                      '//div[contains(@class, "OrderHistory_textBox")]//p[contains(@class, "text_type_digits-default")]')
    FEED_ORDERS = (By.XPATH,
                   '//div[contains(@class, "OrderHistory_textBox")]//p[contains(@class, "text_type_digits-default")]')
    NUMBER_IN_PROGRESS = (By.XPATH,
                          './/ul[contains(@class, "OrderFeed_orderListReady")]/li[contains(@class, "text_type_digits-default")]')
    TOTAL_ORDER_COUNT = (By.XPATH, '//p[text()="Выполнено за все время:"]/following-sibling::p')
    DAILY_ORDER_COUNT = (By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p')