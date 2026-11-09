class upi():
    def withdrawal(self):
        print("withdraw through upi")
class creditcard(upi):
    def withdrawal(self):
        print("withdraw through creditcard")
class Netbanking(upi,creditcard):
    def withdrawal(self):
        print("withdrawal through Netbanking")
def payment(self):
    self.withdrawal()
a=upi()
b=creditcard()
c=Netbanking()
payment(a)
payment(b)
payment(c)