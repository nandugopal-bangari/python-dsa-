class bankacc:
    holderName="mohan"
    accNo="6543254238696"
    balance=6542750.00
    def deposit(self,amount):
        total=amount+self.balance
        print(amount,"money deposited",total)
    def withdraw(self,cash):
        bal=self.balance-cash
        print(cash,"money withdrawed",bal)
    def display_balance(self):
        print(self.balance)
b=bankacc()
print(b.holderName)
print(b.accNo)
print(b.balance)
b.deposit(100)
b.withdraw(20)
b.display_balance()