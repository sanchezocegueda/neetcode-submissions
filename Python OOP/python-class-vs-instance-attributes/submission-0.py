class BankAccount: 
    # TODO: Add class and instance attributes at their appropriate places
    
    total_accounts = 0
    total_balance = 0

    def __init__(self, name: str, balance: int) -> None:
        BankAccount.total_accounts += 1
        BankAccount.total_balance += balance
        self.name = name
        self.__balance = balance
    
    @property
    def balance(self) -> int:
        return self.__balance
    
    @balance.setter
    def balance(self, balance: int):
        self.__balance = balance


# TODO: Create two accounts
# TODO: Print the information using the mentioned format

alice = BankAccount("Alice", 1000)
bob = BankAccount("Bob", 2000)

lst = [alice, bob]

for v in lst:
    print(f"{v.name}'s balance: ${v.balance}")

print(f"Total Accounts: {v.total_accounts}")
print(f"Total Balance: ${v.total_balance}")

