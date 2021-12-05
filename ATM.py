class Atm:
    def __init__(self, card_number, pin_number, balance):
        self.card_number = card_number
        self.pin_number = pin_number
        self.balance = balance

    def withdraw(self,amount):
        self.balance = self.balance  - amount

    def deposit(self,amount):
        self.balance = self.balance + amount
    
    def checkBalance(self):
        print('Card Number = ' + str(self.card_number))
        print('Available Balance = ' + str(self.balance))

    def info(self):
        print(self.card_number, self.pin_number, self.balance)

def main():
    atm = Atm('1234578', '2021', 999999)
    atm.withdraw(10000)
    atm.checkBalance()
    atm.deposit(8000)
    atm.checkBalance()

main()