

class BankAccount:
    def __init__(self, account_number, holder, balance):
        self.account_number = account_number
        self.holder = holder
        self.balance = balance
    def display(self):
        print("Account Number:", self.account_number)
        print("Account Holder:", self.holder)
        print("Balance: ₹", self.balance)
        print("---------------------------")
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposit of ₹", amount, "successful.")
        else:
            print("Invalid deposit amount!")
        print("Updated Balance: ₹", self.balance)
        print("---------------------------")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance! Withdrawal failed.")
        elif amount <= 0:
            print("Invalid withdrawal amount!")
        else:
            self.balance -= amount
            print("Withdrawal of ₹", amount, "successful.")
        print("Updated Balance: ₹", self.balance)
        print("---------------------------")



if __name__ == "__main__":
    acc1 = BankAccount(1001, "Rahul Sharma", 5000)
    acc1.display()
    acc1.deposit(2000)
    acc1.withdraw(1500)
    acc1.display()