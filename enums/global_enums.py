from enum import Enum


class ErrorMessages(Enum):
    NO_SUCCESS_LOGIN_MESSAGE = 'Welcome message is not presented'
    NO_SUCCESS_TRANSACTION_MESSAGE = 'Success message is not presented'
    BALANCE_ERROR = 'Invalid balance'
    INVALID_URL = 'Invalid url'
    NO_CREDIT_TRANSACTION = 'Credit transaction is not presented'
    NO_DEBIT_TRANSACTION = 'Debit transaction is not presented'


class SuccessMessages(Enum):
    WELCOME_MESSAGE = 'Welcome Harry Potter !!'
    SUCCESS_WITHDRAWL = 'Transaction successful'
    SUCCESS_DEPOSIT = 'Deposit Successful'


class TransactionTypes(Enum):
    DEPOSIT = 'deposit'
    WITHDRAWL = 'withdrawl'
