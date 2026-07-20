class BankAccount:
    def __init__(self, balance: int):
        self.__balance = balance
    
    # TODO: Add getter method for balance
    def get_balance(self):
        return self.__balance
    
    def set_balance(self, balance):
        if balance < 0:
            return print("Cannot set negative balance!")
        
        self.__balance = balance

    # TODO: Add setter method for balance




# Don't modify the code below this line
account = BankAccount(1000)
print(account.get_balance())
account.set_balance(-100)
print(account.get_balance())
account.set_balance(100)
print(account.get_balance())
account.set_balance(0)
print(account.get_balance())
