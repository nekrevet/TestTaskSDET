from pages.base_page import BasePage
from pages.locators import TransactionsPageLocators
from enums.global_enums import ErrorMessages

import csv
from dateutil import parser


class TransactionsPage(BasePage):
    def should_be_transactions(self):
        assert self.is_element_present(*TransactionsPageLocators.CREDIT_TRANSACTION), \
            ErrorMessages.NO_CREDIT_TRANSACTION.value
        assert self.is_element_present(*TransactionsPageLocators.DEBIT_TRANSACTION), \
            ErrorMessages.NO_DEBIT_TRANSACTION.value

    def generate_csv(self):
        credit_date = parser.parse(self.browser.find_element(
            *TransactionsPageLocators.CREDIT_DATE).text).strftime('%d %B %Y %H:%M:%S')
        debit_date = parser.parse(self.browser.find_element(
            *TransactionsPageLocators.DEBIT_DATE).text).strftime('%d %B %Y %H:%M:%S')
        transactions = [
            [
                ' '.join(
                        (credit_date,
                         self.browser.find_element(*TransactionsPageLocators.CREDIT_SUM).text,
                         self.browser.find_element(*TransactionsPageLocators.CREDIT_TYPE).text))
            ],
            [
                ' '.join(
                        (debit_date,
                         self.browser.find_element(*TransactionsPageLocators.DEBIT_SUM).text,
                         self.browser.find_element(*TransactionsPageLocators.DEBIT_TYPE).text))
            ]
        ]
        with open('transactions.csv', 'w', newline='') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_NONE)
            writer.writerows(transactions)
