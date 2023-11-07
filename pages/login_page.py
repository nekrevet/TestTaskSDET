from pages.base_page import BasePage
from pages.locators import LoginPageLocators, AccountPageLocators
from enums.global_enums import ErrorMessages, SuccessMessages

from selenium.webdriver.support.ui import Select
import allure


class LoginPage(BasePage):
    @allure.step('login as customer')
    def login(self):
        with allure.step('click on customer login button'):
            self.browser.find_element(*LoginPageLocators.CUSTOMER_LOGIN_BTN).click()
        with allure.step("choose customer's name"):
            name_select = Select(self.browser.find_element(*LoginPageLocators.NAME_SELECT))
            name_select.select_by_value('2')
        with allure.step('click on submit button'):
            self.browser.find_element(*LoginPageLocators.SUBMIT_BTN).click()
        with allure.step('check that welcome message is presented'):
            welcome_msg = self.browser.find_element(*AccountPageLocators.WELCOME_MSG).text
            assert welcome_msg == SuccessMessages.WELCOME_MESSAGE.value, ErrorMessages.NO_SUCCESS_LOGIN_MESSAGE.value
