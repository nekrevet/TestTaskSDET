from pages.base_page import BasePage
from pages.locators import AccountPageLocators
from enums.global_enums import ErrorMessages, SuccessMessages, TransactionTypes
from fibonacci import Amount

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class AccountPage(BasePage):
    @allure.step('make transaction {tr_type}')
    def transaction(self, tr_type):
        if tr_type == TransactionTypes.DEPOSIT.value:
            with allure.step('click on deposit button'):
                self.browser.find_element(*AccountPageLocators.DEPOSIT_BTN).click()
            with allure.step('enter amount in field'):
                self.browser.find_element(*AccountPageLocators.AMOUNT_D_INPUT).send_keys(str(Amount.AMOUNT))
        else:
            with allure.step('click on withdrawl button'):
                self.browser.find_element(*AccountPageLocators.WITHDRAWL_BTN).click()
            with allure.step('enter amount in field'):
                self.browser.find_element(*AccountPageLocators.AMOUNT_W_INPUT).send_keys(str(Amount.AMOUNT))
        with allure.step('click on submit button'):
            self.browser.find_element(*AccountPageLocators.SUBMIT_BTN).click()
        with allure.step('check that success message is presented'):
            success_msg = self.browser.find_element(*AccountPageLocators.SUCCESS_MSG).text
            assert success_msg == SuccessMessages.SUCCESS_DEPOSIT.value if tr_type == TransactionTypes.DEPOSIT.value \
                else SuccessMessages.SUCCESS_WITHDRAWL, \
                ErrorMessages.NO_SUCCESS_TRANSACTION_MESSAGE.value

    @allure.step('check that balance is 0')
    def check_balance(self):
        balance = self.browser.find_element(*AccountPageLocators.BALANCE).text
        assert balance == '0', ErrorMessages.BALANCE_ERROR.value

    @allure.step('go to transaction page')
    def go_to_transaction_page(self):
        with allure.step('click on transactions button'):
            self.browser.find_element(*AccountPageLocators.TRANSACTIONS_BTN).click()
        with allure.step('check that transaction page is opened'):
            WebDriverWait(self.browser, 5).until(EC.url_contains('listTx'))
            assert 'listTx' in self.browser.current_url, ErrorMessages.INVALID_URL.value
