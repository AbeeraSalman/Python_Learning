class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name)


class Dog(Animal):
    def speakDog(self):
        self.name = input("What is your name? ")
        print(self.name)


obj = Animal("Bob")
obj.speak()

obj1 = Dog("Tommy")
obj1.speak()
obj1.speakDog()                   