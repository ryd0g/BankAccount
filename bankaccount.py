class BankAccount:
    def __init__(self, full_name, account_number, routing_number, balance):
        self.full_name = full_name
        self.account_number = account_number
        self.routing_number = routing_number
        self.balance = balance

    def deposit(self, amount):
        total = balance + amount
        print(f"Amount Deposited: ${self.amount}")

    def withdraw(self, amount):
        total = balance - amount
        if amount > balance:
            print(f"Insufficient Funds. You have been charged an overdraft fee of $10")
        else:
            print(f"Amount Withdrawn: ${self.amount}")

    def get_balance(self):
        return self.balance
        print(f"Your balance is ${self.balance}")
    
    def add_interest(self):
        interest = balance * 0.00083
        print(f"Your monthly interest is ${self.interest}")

    def print_receipt(self):
        receipt = [full_name, account_number, routing_number, balance]
        print(receipt)
