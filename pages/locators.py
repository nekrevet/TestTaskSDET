from selenium.webdriver.common.by import By


class LoginPageLocators:
    CUSTOMER_LOGIN_BTN = By.CSS_SELECTOR, '[ng-click="customer()"]'
    NAME_SELECT = By.CSS_SELECTOR, '[name="userSelect"]'
    SUBMIT_BTN = By.CSS_SELECTOR, '[type="submit"]'


class AccountPageLocators:
    WELCOME_MSG = By.XPATH, '//div[contains(@class, "borderM")]/div[1]/strong[1]'
    DEPOSIT_BTN = By.CSS_SELECTOR, '[ng-click="deposit()"]'
    AMOUNT_D_INPUT = By.CSS_SELECTOR, '[type="number"]'
    AMOUNT_W_INPUT = By.XPATH, '//label[text()="Amount to be Withdrawn :"]//following-sibling:: input'
    SUBMIT_BTN = By.CSS_SELECTOR, '[type="submit"]'
    SUCCESS_MSG = By.CSS_SELECTOR, '[ng-show="message"]'
    WITHDRAWL_BTN = By.CSS_SELECTOR, '[ng-click="withdrawl()"]'
    BALANCE = By.XPATH, '//div[contains(@class, "borderM")]/div[2]/strong[2]'
    TRANSACTIONS_BTN = By.CSS_SELECTOR, '[ng-click="transactions()"]'


class TransactionsPageLocators:
    CREDIT_TRANSACTION = By.CSS_SELECTOR, 'tbody > tr:nth-child(1)'
    DEBIT_TRANSACTION = By.CSS_SELECTOR, 'tbody > tr:nth-child(2)'
    CREDIT_DATE = By.CSS_SELECTOR, 'tbody > tr:nth-child(1) > td:nth-child(1)'
    CREDIT_SUM = By.CSS_SELECTOR, 'tbody > tr:nth-child(1) > td:nth-child(2)'
    CREDIT_TYPE = By.CSS_SELECTOR, 'tbody > tr:nth-child(1) > td:nth-child(3)'
    DEBIT_DATE = By.CSS_SELECTOR, 'tbody > tr:nth-child(2) > td:nth-child(1)'
    DEBIT_SUM = By.CSS_SELECTOR, 'tbody > tr:nth-child(2) > td:nth-child(2)'
    DEBIT_TYPE = By.CSS_SELECTOR, 'tbody > tr:nth-child(2) > td:nth-child(3)'
