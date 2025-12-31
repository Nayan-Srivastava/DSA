class BankAccount:
    def __init__(self, account_holder, initial_balance):
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        return f"Deposited: ${amount:.2f}. New balance: ${self.balance:.2f}"

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds for withdrawal.")
        self.balance -= amount
        return f"Withdrew: ${amount:.2f}. New balance: ${self.balance:.2f}"

    def transfer(self, target_account, amount):
        if amount < 0:
            raise ValueError("Transfer amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds for transfer.")
        self.balance -= amount
        target_account.balance += amount
        return f"Transferred: ${amount:.2f} to {target_account.account_holder}. New balance: ${self.balance:.2f}"

# Example usage:
account1 = BankAccount("Alice", 1000)
account2 = BankAccount("Bob", 500)
print(account1.deposit(200))          # Deposited: $200.00. New balance: $1200.00
print(account1.withdraw(150))         # Withdrew: $150.00. New balance: $1050.00
print(account1.transfer(account2, 300))  # Transferred: $300.00 to Bob. New balance: $750.00
print(f"Bob's new balance: ${account2.balance:.2f}")  # Bob's new balance: $800.00