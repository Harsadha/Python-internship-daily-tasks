# bank class from day 3 to be tested by bank_test.py using pytest

import re

class BankAccount:
    bank_name = "ICICI"
    minimum_balance = 500
    acc_no = 1000

    def __init__(self,name,balance,pin):
        self.acc_no = BankAccount.acc_no
        BankAccount.acc_no+=1
        self.name = name
        self.balance = balance
        self.pin = pin
    
    @property
    def balance(self):
        return self._balance

    def get_balance(self,input_pin):
        if self._pin==input_pin:
            return self._balance
        raise ValueError("Entered the pin wrong. :/")
    
    @balance.setter
    def balance(self,value):
        if value<BankAccount.minimum_balance:
            raise ValueError("Balance should not be less than the minimum balance :/")
        else:
            self._balance = value

    @property
    def pin(self):
        return self._pin
    
    @pin.setter
    def pin(self,input_pin):
        if re.fullmatch(r"\d{4}", input_pin):
            self._pin = input_pin
        else:
            raise ValueError("Enter a valid 4 digit pin")

    def deposit(self,deposit_amount):
        self._balance +=deposit_amount
        print("Deposited Rs.",deposit_amount)

    def withdraw(self,withdrawl_amount,input_pin):
        if self._pin == input_pin:
            if self._balance >= withdrawl_amount+self.minimum_balance:
                self._balance -= withdrawl_amount
                print("Withdrew Rs.",withdrawl_amount)
            else:
                raise ValueError("Cannot withdraw more than your balance. Make sure you have the minimum balance.")
        else:
            raise ValueError("Wrong pin entered. :/")
            
    @classmethod
    def from_dict(cls,data):
        return cls(data["name"],data["balance"],data["pin"])
    
    def __str__(self):
        return f"Account number:{self.acc_no}\t Name:{self.name}\t"
