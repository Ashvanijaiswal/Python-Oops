import datetime
import csv
class BankAccount:
    MIN_BALANCE=-10000

    def __init__(self,owner,account_number,balance=0):
        self.owner=owner
        self.account_number=account_number
        self.created_at = datetime.datetime.now().date()
        if(balance<self.MIN_BALANCE):
            raise ValueError("Balance to small")
        else:
            self.balance=balance
   
    def __eq__(self,other):
        if(self.account_number==other.account_number):
            return True
        else:
            return False


    @classmethod
    def from_csv(cls, filepath):
        with open(filepath, "r") as f:
            row = csv.reader(f).__next__()
            owner, account_number,balance = row
        return cls(owner, account_number,int(balance))

    @property
    def balance(self):
        return self.balance
    @property
    def account_number(self):
        return self.account_number
    @property
    def created_at(self):
        return self.created_at
    
    @balance.setter
    def balance(self,new_balance):
        if new_balance < self.__MIN_BALANCE:
            raise ValueError("Balance to small!")
        else:
            self.balance = new_balance

my_account = BankAccount.from_csv("testfile.csv")
my_account2 = BankAccount.from_csv("testfile.csv")
print(my_account.MIN_BALANCE)
print(my_account==my_account2)
print(my_account.owner, my_account.account_number, my_account.balance)