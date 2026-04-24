import pytest
import allure
import requests
from selenium import webdriver

from pages import UIWorkerWeb
from locators import UIWorkerLocators
from config import BASE_URL, ENDPOINTS
from data.data_generator import generate_user_payload


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    """
    Фикстура для запуска тестов в разных браузерах (Chrome и Firefox).
    Открывает главную страницу приложения перед тестом и закрывает браузер после.
    Параметризирована для запуска каждого теста в обоих браузерах.
    """
    browser_name = request.param
    if browser_name == 'chrome':
        browser = webdriver.Chrome()
    elif browser_name == 'firefox':
        browser = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")
    with allure.step(f'Перейти на Главную страницу'):
        browser.get(BASE_URL)
    yield browser
    browser.quit()


@pytest.fixture()
def pages(driver):
    """
    Возвращает объект страницы (UIWorkerWeb), инициализированный с драйвером и локаторами.
    Используется для взаимодействия с UI через методы страницы.
    """
    return UIWorkerWeb(driver, UIWorkerLocators())


@pytest.fixture
def user_for_test():
    """
    Создаёт пользователя перед тестом и удаляет его после.
    Передает в тест словарь с данными пользователя.
    """
    user_payload = generate_user_payload()
    with allure.step(f'Создать пользователя с email "{user_payload['email']}"'):
        r = requests.post(f"{BASE_URL}{ENDPOINTS['CREATE_USER']}", user_payload)
        token = r.json()['accessToken']
        email = user_payload['email']
        password = user_payload['password']
        name = user_payload['name']
    # Передача данных в тест
    yield {'token': token, 'email': email, 'password': password, 'name': name}

    # После теста удаляем пользователя
    with allure.step('После теста - Удалить пользователя'):
        requests.delete(f"{BASE_URL}{ENDPOINTS['DELETE_USER']}", headers={'Authorization': f'{token}'})


@pytest.fixture()
def login_user(pages, user_for_test):
    """
    Авторизует пользователя через UI (форму входа) перед тестом.
    Использует учётные данные из фикстуры user_for_test.
    Возвращает объект страницы (pages) в состоянии после успешного входа.
    """
    user_data = user_for_test
    with allure.step(f'Авторизоваться под пользователем с email "{user_data['email']}"'):
        pages.login(user_data['email'], user_data['password'])
    return pages


@pytest.fixture()
def created_order(pages, login_user):
    """
    Создаёт заказ через UI и возвращает его ID.
    Использует фикстуру авторизации пользователя
    """
    order_id = pages.create_order()
    return order_id