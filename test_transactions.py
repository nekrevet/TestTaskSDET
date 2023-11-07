from config import SERVICE_URL
from pages.login_page import LoginPage
from pages.account_page import AccountPage
from pages.transactions_page import TransactionsPage
from enums.global_enums import TransactionTypes

import allure


@allure.title('Checking user making transactions')
def test_user_can_make_transactions(browser, fixture_with_attachment_in_finalizer):
    page = LoginPage(browser, SERVICE_URL)
    page.open()
    page.login()
    page = AccountPage(browser, browser.current_url)
    page.transaction(TransactionTypes.DEPOSIT.value)
    page.transaction(TransactionTypes.WITHDRAWL.value)
    page.check_balance()
    page.go_to_transaction_page()
    page = TransactionsPage(browser, browser.current_url)
    page.should_be_transactions()
