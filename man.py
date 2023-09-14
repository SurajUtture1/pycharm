import sys


class Customer:
    '''Customer class to describe bank operations:'''
    bankname = "DurgaBank"

    def __init__(self, name, balance=0.0):
        self.name = name
        self.balance = balance

    def deposit(self, amt):
        self.balance = self.balance + amt
        print('Balance after deposit: ', self.balance)

    def withdraw(self, amt):
        if amt > self.balance:
            print('Insufficient funds ..... can not perform this Operation')
            sys.exit()
        self.balance = self.balance - amt
        print('Balance after withdraw: ', self.balance)


print("Welcome to: ", Customer.bankname)
name = input("Enter customer name: ")
c = Customer(name)

while True:
    print('d - Deposit\nw - Withdraw\ne - Exit')
    option = input("choose your option: ")
    if option.lower() == 'd':
        amount = float(input("Enter amount to deposit: "))
        c.deposit(amount)
    elif option.lower() == 'w':
        amount = float(input("Enter amount to withdraw: "))
        while amount % 500 != 0:
            print('Amount should be multiple of 500')
            amount = float(input("Enter amount to withdraw: "))
        c.withdraw(amount)
    elif option.lower() == 'e':
        print("Thanks for banking")
        sys.exit()
    else:
        print("Invalid Option, choose correct option")
