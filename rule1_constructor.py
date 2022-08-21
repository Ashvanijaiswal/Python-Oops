import datetime
class BankAccount:

    """
    A class used to represent an bank account.

    Attributes
    ----------
    __MIN_BALANCE : int
        minimum allowed balance

    Methods
    -------
    deposit(amount=0)
        addas amount to balance
    withdraw(amount=0)
        subtracts amount from balance
    from_csv(filepath)
        returns class instance from csv file
    """
    

    _bank_name='ICICI'
    #6: Decide what is internal and private
    # A leading underscore is used for naming internal methods and attributes, while a double leading underscore marks private ones
    __MIN_BALANCE=-10000
    def __init__(self, owner, account_number, balance=0):
        self.owner = owner    
        self.account_number = account_number
        self.created_at = datetime.datetime.now().date()
        if balance < self.__MIN_BALANCE:
            raise ValueError("Balance to small!")
        else:
            self._balance = balance
    # Rule 4 -make a string implemention of object
    def __str__(self):
        return f"""
        Bank Account:
            Account Owner:{self.owner}
            Account Number:{self.account_number}
            Creation Date:{BankAccount.to_dash_date(str(self.created_at))}
            Current Balance:{self._balance}
        """
    # Rule 3- Object shoud be same if all attributes are equals to each other. 
    def __eq__(self,other):
        if(self.account_number==other.account_number):
            return True
        else:
            return False

    #5: Know what is static
    @staticmethod
    def to_dash_date(date):
        return date.replace("-", "/") 

    #6: Decide what is internal and private
    # A leading underscore is used for naming internal methods and attributes, while a double leading underscore marks private ones


    def deposit(self, amount):
        self._balance += amount
        
    def withdraw(self, amount):
        if(self._balance>amount):

            self._balance -= amount
        else:
            raise ValueError("Insufficient Amount")

    #7: Set access to attributes
    @property
    def balance1(self):
        return self._balance
    @property
    def accoun_number(self):
        return self.account_number
    @property
    def create_at(self):
        return self.created_at
    
    @balance1.setter
    def balance(self,new_balance):
        if new_balance < self.__MIN_BALANCE:
            raise ValueError("Balance to small!")
        else:
            self._balance = new_balance

my_account=BankAccount("Ashvani",2113,82222)
my_account2=BankAccount("Ashvani",2113,82222)
my_account.balance=1000
my_account.deposit(1000)
my_account.accoun_number=115
# my_account.withdraw(10000)
# or we can also access instance method through class_name by passing object as parameter in instance method
# BankAccount.deposit(my_account,1000)
print(my_account.owner,my_account.account_number,my_account._balance)
print(my_account)
print(my_account._bank_name)
print(my_account2==my_account)

