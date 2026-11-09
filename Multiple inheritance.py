class animal:
    def eat(self):
        print("animal eat")
class mammal:
    def sleep(self):
        print("mammal sleep")
class sheep(animal,mammal):
    def wool(self):
        print("sheep gives wool")
d1=sheep()
d1.eat()
d1.sleep()
d1.wool()

    