class BankAccount:
    account_counter = 1

    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0
        self.account_number = BankAccount.account_counter
        BankAccount.account_counter += 1

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount} to {self.account_holder}'s account.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew ${amount} from {self.account_holder}'s account.")
            else:
                print("Insufficient funds for withdrawal.")
        else:
            print("Withdrawal amount must be positive.")

    def display_balance(self):
        print(f"{self.account_holder}'s current balance: ${self.balance}")

    def transfer(self, amount, other_account):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                other_account.deposit(amount)
                print(f"Transferred ${amount} from {self.account_holder}'s account to {other_account.account_holder}'s account.")
            else:
                print("Insufficient funds for transfer.")
        else:
            print("Transfer amount must be positive.")

 
account1 = BankAccount("Srushti")
account2 = BankAccount("Priya")
 
print("Account 1 Number:", account1.account_number)
print("Account 2 Number:", account2.account_number)
 
account1.deposit(1000)
account2.deposit(500)

 
account1.display_balance()
account2.display_balance()
 
account1.withdraw(200)
 
account1.transfer(300, account2)
 
account1.display_balance()
account2.display_balance()