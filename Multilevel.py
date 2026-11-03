class Animal:
    def eat(self):
        print("Eating")

class Dog(Animal):
    def bark(self):
        print("Woof")

class Puppy(Dog):
    def weep(self):
        print("Weeping")

p = Puppy()
p.eat()
p.bark()
p.weep()