# bank_account.py

class BankAccount:
    def __init__(self, account_name, balance=0):
        self.account_name = account_name
        self.__balance = balance  # Encapsulation

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} deposited. New balance: {self.__balance}")
        else:
            print("Deposit must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"{amount} withdrawn. New balance: {self.__balance}")
        else:
            print("Insufficient balance or invalid amount.")

    def get_balance(self):
        return self.__balance

    def __str__(self):
        return f"BankAccount({self.account_name}, Balance: {self.__balance})"

# Example usage
if __name__ == "__main__":
    acc1 = BankAccount("Hizar", 1000)
    print(acc1)
    acc1.deposit(500)
    acc1.withdraw(200)
    print("Final Balance:", acc1.get_balance())
