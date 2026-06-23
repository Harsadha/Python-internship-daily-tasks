# testing the bank.py of day 3 using pytest

import pytest
from bank import BankAccount

# fixture to creates reusable account
@pytest.fixture
def account():
    return BankAccount("Harsadha",9000,"9090")

# test account creation
def test_account_creation(account):
    assert account.name == "Harsadha"
    assert account.balance == 9000
    assert account.pin == "9090"

# parametrize deposit testing
@pytest.mark.parametrize("amount,expected",[(1000,10000),(500,9500),(2000,11000)])

def test_deposit(account, amount, expected):
    account.deposit(amount)
    assert account.balance == expected

# parametrize withdraw testing
@pytest.mark.parametrize("amount,expected",[(1000,8000),(2000,7000),(500,8500)])

def test_withdraw(account, amount, expected):
    account.withdraw(amount, "9090")
    assert account.balance == expected

# insufficient balance test
def test_insufficient_funds(account):
    with pytest.raises(ValueError):
        account.withdraw( 9000,"9090")

# wrong pin test
def test_wrong_pin(account):
    with pytest.raises(ValueError):
        account.withdraw( 500, "1234")

# property test
def test_balance_property(account):
    assert account.balance == 9000

# from_dict classmethod test
def test_create_from_dict():
    data = {
        "name":"Test User",
        "balance":5000,
        "pin":"1234"
    }
    account = BankAccount.from_dict(data)
    assert account.name == "Test User"
    assert account.balance == 5000

# __str__ test
def test_string(account):
    result = str(account)
    assert "Harsadha" in result