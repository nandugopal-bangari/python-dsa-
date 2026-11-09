class animal:
    def speak(self):
        print("animal speak")
class Dog(animal):
    def speak(self):
        print("dog bark")
d1=Dog()
d1.speak()