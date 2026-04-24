from selenium.webdriver.common.by import By


class MainPageLocators:
    PROFILE_BUTTON = (By.XPATH, './/p[text()="Личный Кабинет"]')
    LOGIN_PROFILE_BUTTON = (By.XPATH, './/button[text()="Войти в аккаунт"]')
    CONSTRUCTOR_BUTTON = (By.XPATH, '//p[text()="Конструктор"]/parent::a')
    CREATE_BURGER_TITLE = (By.XPATH, '//h1[text()="Соберите бургер"]')
    ORDER_FEED_BUTTON = (By.XPATH, '//p[text()="Лента Заказов"]/parent::a')
    FIRST_INGREDIENT = (By.XPATH, '(//a[contains(@class, "BurgerIngredient_ingredient")])[1]')
    INGREDIENT_DETAILS_POPUP = (By.XPATH, '//h2[text()="Детали ингредиента"]')
    CLOSE_POPUP_DETAILS = (By.XPATH, '//button[contains(@class,"close")]')
    ORDER_BASKET = (By.XPATH, '//span[@class="constructor-element__text" and text()="Перетяните булочку сюда (низ)"]')
    INGREDIENT_COUNTER = (By.XPATH, '//ul[1]/a[1]//p[contains(@class, "num")]')
    CONFIRM_ORDER_BUTTON = (By.XPATH, '//button[text()="Оформить заказ"]')
    ORDER_ID = (By.CLASS_NAME, 'Modal_modal__title_shadow__3ikwq')
    CLOSE_POPUP_ORDER = (By.XPATH, '//button[contains(@class, "Modal_modal__close")][1]')