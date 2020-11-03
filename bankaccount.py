class BankAccount:
    #initializing class properties for BankAccount
    def __init__(self, full_name, account_number, routing_number, balance):
        self.full_name = full_name
        self.account_number = account_number
        self.routing_number = routing_number
        self.balance = balance

    #method for deposit (amount), prints statement with new balance
    def deposit(self, amount):
        total = self.balance + amount
        self.balance = total
        print(f'Amount Deposited: ${amount}. Your new balance is ${self.balance}\n')

    #method for withdraw (amount), prints statement with new value
    def withdraw(self, amount):
        total = self.balance - amount
        self.balance = total
        #if (amount) is > balance, prints overdraft message
        if amount > self.balance:
            print(f"Insufficient Funds. You have been charged an overdraft fee of $10")
        else:
            print(f'Amount Withdrawn: ${amount}. Your new balance is ${self.balance}\n')

    #prints balance of customer 
    def get_balance(self):
        print(f"Your balance is ${self.balance}\n")
    
    #takes balance and multiplies for interest, and prints statement 
    def add_interest(self):
        interest = self.balance * 0.00083
        print(f"Your monthly interest is ${interest}\n")

    #prints a receipt for the user
    def print_receipt(self):
        #prints thank you message first, indents, then prints bank account info for user
        receipt = [self.full_name, 'Account No.: ****' + str(self.account_number[-4:]), 
        'Routing No.: ' + str(self.routing_number), 'Balance: $' + str(self.balance)]
        print('Thank you for using PythonBank!')
        for i in receipt:
            print(i)

# #first customer demo
customer_one = BankAccount('Ryan Lee', '29573942', '968473963', 1000)
print(f'Good Morning Mr.{customer_one.full_name[5:8]}!\n')
customer_one.get_balance()
customer_one.deposit(100)
customer_one.print_receipt()

# #second customer demo
customer_two = BankAccount('Jeff Bezos', '06939531', '206927539', 203000000000)
print(f'Good Afternoon Mr.{customer_two.full_name[5:10]}!\n')
customer_two.get_balance()
customer_two.add_interest()
customer_two.print_receipt()

# #third customer demo
customer_three = BankAccount('Donald Trump', '95846212', '235723468', 2500000000)
print(f'Good Evening Mr.{customer_three.full_name[7:12]}!\n')
customer_three.get_balance()
customer_three.withdraw(1000000)
print("Here's a small loan of a million dollars.\n")
customer_three.print_receipt()