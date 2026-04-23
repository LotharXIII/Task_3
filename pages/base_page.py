import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from config import BASE_URL


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_page(self, url=None):
        full_url = BASE_URL + url if url else BASE_URL
        self.driver.get(full_url)

    @allure.step('Получить текущий URL страницы')
    def get_current_url(self):
        current_url = self.driver.current_url
        return current_url

    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    def click_button(self, locator):
        self.driver.find_element(*locator).click()

    def find_element(self, locator):
        return self.wait.until(ec.presence_of_element_located(locator))

    def get_all_elements(self, locator):
        return self.wait.until(ec.presence_of_all_elements_located(locator))

    def get_element_text(self, locator):
        element = self.find_element(locator)
        return element.text

    def input_text(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    def check_element_displayed(self, locator):
        return self.wait.until(ec.visibility_of_element_located(locator))

    def check_presence_element(self, locator):
        self.wait.until(ec.presence_of_element_located(locator))
        return self.driver.find_element(*locator)

    def check_element_not_displayed(self, locator):
        return self.wait.until(ec.invisibility_of_element(locator))

    def element_is_clickable(self, locator):
        self.wait.until(ec.element_to_be_clickable(locator))

    def drag_and_drop_on_element(self, locator_one, locator_two):
        draggable = self.driver.find_element(*locator_one)
        droppable = self.driver.find_element(*locator_two)
        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(draggable, droppable).perform()