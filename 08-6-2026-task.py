# DAILY TASK- WEEK 1- DAY 3
'''
Build a BankAccount class:
✓ Owner name and balance as instance variables 
✓ deposit() and withdraw() methods (block insufficient funds)
✓ @property for read-only balance
✓ @classmethod to create account from a dict
✓ Clean summary using __str__'''

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

#main func
print("Bank:",BankAccount.bank_name) #class instance
print("Welcome to the bank portal!")
print("\nMENU:\n1.Create a bank account\n2.View your balance\n3.Deposit amount\n4.Withdraw amount\n5.Show account\n0.Exit")
Bank_Accounts = {}
while(1):
    print()
    choice = int(input("Enter your choice:"))
    if choice==0:
        print("Exiting...")
        break
    elif choice==1: # create an account
        try:
            name = input("Enter the bank account holder's name(eg: Inde Navarette):")
            pattern = r"^[A-Za-z]+ ([A-Za-z])*$"
            if not re.match(pattern, name):
                print("Please enter a valid name.")
                continue
            balance = int(input("Enter your balance amount:"))
            pin = input("Enter a 4 digit pin(eg:9999):")
            bank_account = BankAccount(name,balance,pin)
            Bank_Accounts[bank_account.acc_no]=bank_account
            print("Account created successfully!\n***Account number:",bank_account.acc_no,"***")
        except Exception as e:
            print("Error:",e)
            continue
        # try:
        #     bank_account = BankAccount("Harsadh R",90000,"0108")
        #     Bank_Accounts[bank_account.acc_no]=bank_account
        #     bank_account = BankAccount("Sruthi R",60000,"1411")
        #     Bank_Accounts[bank_account.acc_no]=bank_account
        #     bank_account = BankAccount("Hari Sankar",100000,"0609")
        #     Bank_Accounts[bank_account.acc_no]=bank_account
        #     bank_account = BankAccount("Ranjeeth Kumar",200000,"2011")
        #     Bank_Accounts[bank_account.acc_no]=bank_account
        #     bank_account = BankAccount("Visalakshi",990,"0209")
        #     Bank_Accounts[bank_account.acc_no]=bank_account
        # except Exception as e:
        #     print("Error:",e)
            
    elif choice==2: # view balance
        print("Viewing Balance")
        try:
            acc_no = int(input("Enter your account number:"))
            bank_account = Bank_Accounts.get(acc_no)
            if not bank_account:
                print("Enter your valid account number.")
                continue
            input_pin = input("Enter your pin:")
            print("Balance amount:",bank_account.get_balance(input_pin))
        except Exception as e:
            print("Error:",e)
            continue
        
    elif choice==3: # Deposit
        print("Depositing money")
        try:
            acc_no = int(input("Enter the account number to deposit money to:"))
            bank_account = Bank_Accounts.get(acc_no)
            if not bank_account:
                print("Enter your valid account number.")
                continue
            
            print("Please verify the account details you are depositing money to:\n",Bank_Accounts[acc_no])
            deposit_amount = float(input("Enter the amount to be deposited to your account:"))
            bank_account.deposit(deposit_amount)
        except Exception as e:
            print("Error:",e)
            continue

    elif choice==4: # withdraw
        print("Withdrawing money from your account")
        try:
            acc_no = int(input("Enter your account number:"))
            bank_account = Bank_Accounts.get(acc_no)
            if not bank_account:
                print("Enter your valid account number.")
                continue
            input_pin = input("Enter your pin:")
            withdraw_amount = float(input("Enter the amount to be withdrawn from your account:"))
            bank_account.withdraw(withdraw_amount,input_pin)
        except Exception as e:
            print("Error:",e)
            continue
        
    elif choice==5: # Viewing account details
        print("Viewing all the account details")
        for acc_no in Bank_Accounts:
            print(Bank_Accounts.get(acc_no))

data = {"name":"Harsadha","balance":9000,"pin":"9090"}
bank =BankAccount.from_dict(data)
print(bank)