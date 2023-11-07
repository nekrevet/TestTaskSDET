from pages.base_page import BasePage
from pages.locators import TransactionsPageLocators
from enums.global_enums import ErrorMessages

import allure


class TransactionsPage(BasePage):
    @allure.step("check that user's transactions are presented")
    def should_be_transactions(self):
        with allure.step('check that credit transaction is presented'):
            assert self.is_element_present(*TransactionsPageLocators.CREDIT_TRANSACTION), \
                ErrorMessages.NO_CREDIT_TRANSACTION.value
        with allure.step('check that debit transaction is presented'):
            assert self.is_element_present(*TransactionsPageLocators.DEBIT_TRANSACTION), \
                ErrorMessages.NO_DEBIT_TRANSACTION.value
