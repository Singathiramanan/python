class BankAccount:
    interest_rate = 0.04    # class variable
    def __init__(self, name, balance):
        # instance variables 
        self.name = name
        self.balance = balance
        self.transactions = [ ]
        self.transactions.append(f'Inital amount deposited ${balance}')
    
    def __str__(self):
        return f"{self.name}'s Account"
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        self.transactions.append(f"Amount deposited ${amount}")

    def withdraw(self, amount):
        self.balance = self.balance - amount
        self.transactions.append(f"Amount withdrawn ${amount}")
    
    def statement(self):
        for item in self.transactions:
            print(item)
        print("*" * 20)
        print(f'Total available balance ${self.balance}')
    
    def transfer(from_account, to_account, amount):
        if from_account.balance < amount:
            raise ValueError("Not enough funds")
        to_account.balance += amount
        from_account.balance -= amount
        from_account.transactions.append(f"Amount ${amount} transferred to {to_account}")
    
    def roi(self):
        # int_amount = self.balance * BankAccount.interest_rate
        int_amount = self.balance * self.__class__.interest_rate
        self.balance = self.balance + int_amount

c1 = BankAccount('steve', 1000)
c2 = BankAccount('bill', 2000)

# c1.transfer(c2, 100)        # BankAccount.transfer(c1, c2, 100)