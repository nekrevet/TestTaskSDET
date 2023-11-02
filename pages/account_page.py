from pages.base_page import BasePage
from pages.locators import AccountPageLocators
from enums.global_enums import ErrorMessages, SuccessMessages, TransactionTypes
from fibonacci import Amount

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AccountPage(BasePage):
    def transaction(self, tr_type):
        if tr_type == TransactionTypes.DEPOSIT.value:
            self.browser.find_element(*AccountPageLocators.DEPOSIT_BTN).click()
            self.browser.find_element(*AccountPageLocators.AMOUNT_D_INPUT).send_keys(str(Amount.AMOUNT))
        else:
            self.browser.find_element(*AccountPageLocators.WITHDRAWL_BTN).click()
            self.browser.find_element(*AccountPageLocators.AMOUNT_W_INPUT).send_keys(str(Amount.AMOUNT))
        self.browser.find_element(*AccountPageLocators.SUBMIT_BTN).click()
        success_msg = self.browser.find_element(*AccountPageLocators.SUCCESS_MSG).text
        assert success_msg == SuccessMessages.SUCCESS_DEPOSIT.value if tr_type == TransactionTypes.DEPOSIT.value \
            else SuccessMessages.SUCCESS_WITHDRAWL, \
            ErrorMessages.NO_SUCCESS_TRANSACTION_MESSAGE.value

    def check_balance(self):
        balance = self.browser.find_element(*AccountPageLocators.BALANCE).text
        assert balance == '0', ErrorMessages.BALANCE_ERROR.value

    def go_to_transaction_page(self):
        self.browser.find_element(*AccountPageLocators.TRANSACTIONS_BTN).click()
        WebDriverWait(self.browser, 5).until(EC.url_contains('listTx'))
        assert 'listTx' in self.browser.current_url, ErrorMessages.INVALID_URL.value
