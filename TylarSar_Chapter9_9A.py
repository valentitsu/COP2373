# Create a bank account that includes name, account num, amount, and interest rate. Include __init__ and __str__ method
class BankAcct:
    def __init__(self, user, accountNum, amount, interest):
        # Define variables
        self.user = user
        self.accountNum = accountNum
        self.amount = amount
        self.interest = interest

    def changeInterest(self, newRate):
        # Makes the interest rate adjustable
        self.interest = newRate

    def deposit(self, amount):
        # Add constraint where user must enter a positive number into deposits
        if amount > 0:
            self.amount += amount
        else:
            print("Amount must be positive.")

    def withdraw(self, amount):
        # Add constraint where user must have enough money for the deposit they're trying to make
        if amount > 0:
            if self.amount >= amount:
                self.amount -= amount
            else:
                print("Lacking Funds.")
        else:
            print("Withdrawal amount must be positive.")

    def balance(self):
        return self.amount

    def calcInterest(self, days):
        return self.amount * (self.interest / 100) * (days / 365)

    def __str__(self):
        return f"Account holder: {self.user}\nAccount number: {self.accountNum}\nBalance: ${self.amount:.2f}\nInterest rate: {self.interest}%"

def test():
    # Account creation and test of different variables
    account = BankAcct("Draco Malfoy", "8529688", 1000.0, 5.0)

    print(account)

    account.deposit(300)
    print("\nAfter depositing $300:")

    print(account)

    account.withdraw(400)
    print("\nAccount after a withdrawal of $400:")

    print(account)

    print(f"\nYour current balance: ${account.balance():.2f}")

    interest = account.calcInterest(30)
    print(f"\nCurrent interest for 30 days: ${interest:.2f}")

    account.changeInterest(4.0)
    print("\nChange in interest to 4.0%:")

    print(account)

# Run the test function
if __name__ == "__main__":
    test()