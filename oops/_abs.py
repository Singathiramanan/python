from abc import ABC, abstractmethod
# design specification it is enforcing the child classes to implement "depost" and "withdraw" method
class Bank(ABC):

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

class HDFCBank(Bank):
    def deposit(self, amount):
        print("Depositing Amount in HDFC bank")
    
    def withdraw(self, amount):
        print("Withdraaing Amount from HDFC Bank")

class SBI(Bank):
    def deposit(self, amount):
        print("Depositing Amount from SBI")
    
    def withdraw(self, amount):
        print("Withdraaing Amount from SBI")

class ICICI(Bank):
    def deposit(self, amount):
        print("Depositing amount to ICICI")
    
    def withdraw(self, amount):
        print("Withdrawing amount from icici")