import sys


class Customer:
    bankname = 'suraj bank'

    def __init__(self, name, balance=0.0):
        self.name = name
        self.balance = balance

    def deposit(self, amt):
        self.balance = self.balance+amt
        print('balance after deposit:', self.balance)

    def withdraw(self, amt):
        if amt > self.balance:
            print('insufficient cannot perform')
            sys.exit()
        self.balance = self.balance - amt
        print('Balance after withdraw:', self.balance)


print('Welcome to', Customer.bankname)
name = input("Enter your name:")
c = Customer(name)

while True:
    print('d - deposit\nw - Withdraw\ne - Exit')
    option = input('Choose your option :')
    if option.lower() == 'd':
        amount = float(input("Enter amount to deposit:"))
        c.deposit(amount)
    elif option.lower() == 'w':
        amount = float(input('Enter amount to withdraw:'))
        if amount % 500 != 0:
            print('amount should be multiples of 500')
            amount=float(input('Enter amount to withdraw'))
        c.withdraw(amount)
    elif option.lower() == 'e':
        print('Thanks for banking')
        sys.exit()

    else:
        print("invalid character identified:, check it once")
