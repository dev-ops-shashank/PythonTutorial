class BankAccount:
    # In Python, we use double underscores (__) to make attributes private:
    def __init__(self, balance):
        self.__balance = balance  # private attribute
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
    
    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
print(account.get_balance())  # Output: 1000
# print(account.__balance)  # This would raise an AttributeError