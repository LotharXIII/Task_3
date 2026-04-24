from locators.auth_page_lct import AuthPageLocators
from locators.main_page_lct import MainPageLocators
from locators.order_feed_page_lct import OrderFeedPageLocators
from locators.profile_page_lct import ProfilePageLocators
from locators.recovery_password_page_lct import RecoveryPasswordPageLocators


class UIWorkerLocators(
    MainPageLocators,
    AuthPageLocators,
    RecoveryPasswordPageLocators,
    OrderFeedPageLocators,
    ProfilePageLocators
):
    pass