class BankAccount:
    def __init__(self,account_number,name, account_type, balance=0):
        self.account_number = account_number
        self.name = name
        self.account_type = account_type
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully. New balance: ₹{self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficient balance. Available balance: ₹{self.balance}")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully. New balance: ₹{self.balance}")

    def display_details(self):
        print("\nAccount Details:")
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.name}")
        print(f"Account Type: {self.account_type}")
        print(f"Balance: ₹{self.balance}")


print("Welcome to the Bank Account Management System")

account_number = input("Enter account number: ")
name = input("Enter account holder's name: ")
account_type = input("Enter account type (Savings/Current): ")
balance = float(input("Enter initial balance: "))

account = BankAccount(account_number, name, account_type, balance)

print("\n1. Display Account Details")
account.display_details()

print("\n2. Deposit Money")
deposit_amount = float(input("Enter amount to deposit: "))
account.deposit(deposit_amount)

print("\n3. Withdraw Money")
withdraw_amount = float(input("Enter amount to withdraw: "))
account.withdraw(withdraw_amount)

print("\n4. Display Updated Account Details")
account.display_details()