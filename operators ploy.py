class Addition:
    def add(self,a,b):
        print(a+b)
class subtraction(Addition):
    def add(self,a,b):
        print(a-b)
a=int(input("Enter a"))
b=int(input("Enter b"))
c=Addition()
c.add(a,b)