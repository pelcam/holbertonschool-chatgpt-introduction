from decimal import Decimal, InvalidOperation

class Checkbook:
    def __init__(self):
        """Initializes the checkbook with a balance of 0.0."""
        self.balance = Decimal('0.00')

    def deposit(self, amount):
        """Deposits a specified amount into the checkbook balance."""
        try:
            amount = Decimal(amount)
            if amount <= 0:
                print("Deposit amount must be positive.")
                return
            self.balance += amount
            print(f"Deposited ${amount:.2f}")
            self.get_balance()
        except InvalidOperation:
            print("Invalid amount. Please enter a valid number.")

    def withdraw(self, amount):
        """Withdraws a specified amount from the checkbook balance if sufficient funds exist."""
        try:
            amount = Decimal(amount)
            if amount <= 0:
                print("Withdrawal amount must be positive.")
                return
            if amount > self.balance:
                print("Insufficient funds to complete the withdrawal.")
            else:
                self.balance -= amount
                print(f"Withdrew ${amount:.2f}")
                self.get_balance()
        except InvalidOperation:
            print("Invalid amount. Please enter a valid number.")

    def get_balance(self):
        """Displays the current balance of the checkbook."""
        print(f"Current Balance: ${self.balance:.2f}")

def main():
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").strip().lower()
        if action == 'exit':
            break
        elif action == 'deposit':
            amount = input("Enter the amount to deposit: $").strip()
            cb.deposit(amount)
        elif action == 'withdraw':
            amount = input("Enter the amount to withdraw: $").strip()
            cb.withdraw(amount)
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
