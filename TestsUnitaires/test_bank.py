from .bank import Account


def test_deposit():
    account = Account(initial_balance=1000)
    account.deposit(1000)
    assert account.balance == 2000


def test_withdraw():
    account = Account(initial_balance=1000)
    account.withdraw(500)
    assert account.balance == 500


def test__create_identifier_length_of_identifier():
    account = Account(initial_balance=1000)
    assert len(account.identifier) == 25


def test__create_identifier_is_alnum():
    account = Account(initial_balance=1000)
    assert account.identifier.isalnum() is True
