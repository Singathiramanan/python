class BankAccount:
    interest_rate = 0.04
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self._transactions = [ ]
    
    def deposit(self, amount):
        self.balance += amount
        self._transactions.append(f"Amount deposited {amount}")
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self._transactions.append(f"Amount withdrawn {amount}")
        else:
            raise Exception("Insufficient Funds")
    
    def statement(self):
        for transaction in self._transactions:
            print(transaction)
        print(f"Total Account Balance {self.balance}")
    
    def roi(self):
        interest_amount = self.balance * self.__class__.interest_rate
        self.balance += interest_amount 

class SavingsBankAccount(BankAccount):
    interest_rate = 0.045
    
    def __init__(self, name, balance):
        super().__init__(name, balance)
        
    def withdraw(self, amount):
        if amount > 10000:
            raise Exception("cannot witdraw more than 10K")
        super().withdraw(amount)
        
class SalaryAccount(BankAccount):
    MAX_DRAFT_AMOUNT = 10000
    def __init__(self, name, balance=0):
        self.is_first_month_pay = True
        self.draft_amount = 0
        super().__init__(name, balance)
    
    def deposit(self, amount):
        if self.is_first_month_pay:     # if self.is_first_month_pay == True
            self.is_first_month_pay = False
            super().deposit(amount + 1000)
        else:
            super().deposit(amount)
        
    def overdraft(self, amount):
        if self.draft_amount + amount <= SalaryAccount.MAX_DRAFT_AMOUNT:
            self.draft_amount += amount
            super().deposit(amount)
        else:
            raise Exception(f"Max draftamount allowed {SalaryAccount.MAX_DRAFT_AMOUNT}")

class SeniorCitizenAccount(BankAccount):
    interest_rate = 0.05

    def withdraw(self, amount):
        if amount > 20000:
            raise Exception("Exceeds daily limit")
        super().withdraw(amount)


class SukanyaSamrudhiAccount(BankAccount):
    interest_rate = 0.095
    def __init__(self, name, balance):
        super().__init__(name, balance)
    
    def deposit(self, amount):
        if amount < 1000:
            raise Exception("Min deposit amount is 1000")
        super().deposit(amount)
    
    def withdraw(self, amount):
        raise Exception("Withdrawal not allowed")

class Parent1(object):
    def demo(self):
        print("Parent1 Demo")
        super().demo()

class Parent2:
    def demo(self):
        print("Parent2 Demo")
        super().demo()

class Child(Parent2, Parent1):
    pass