class BankAccount:
    def __init__(self, full_name, account_number, routing_number, balance):
        self.full_name = full_name
        self.account_number = account_number
        self.routing_number = routing_number
        self.balance = balance

    def deposit(self, amount):
        total = self.balance + amount
        print(f"Amount Deposited: ${amount}. Your balance is ${total}")

    def withdraw(self, amount):
        total = self.balance - amount
        if amount > balance:
            print(f"Insufficient Funds. You have been charged an overdraft fee of $10")
        else:
            print(f"Amount Withdrawn: ${amount}. Your balance is ${total}")

    def get_balance(self):
        print(f"Your balance is ${self.balance}")
    
    def add_interest(self):
        interest = self.balance * 0.00083
        print(f"Your monthly interest is ${interest}")

    def print_receipt(self):
        receipt = [self.full_name, self.account_number, self.routing_number, self.balance]
        for i in receipt:
            print(i)

customer_one = BankAccount('Ryan Lee', '29573942', '968473963', 1000)
customer_two = BankAccount('Jeff Bezos', '06939531', '206927539', 203000000000)
customer_three = BankAccount('Donald Trump', '95846212', '235723468', 2500000000)