from abc import ABC,abstractmethod

class animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class dog(animal):
    def make_sound(self):
        print("Bark!")


class cat(animal):
    def make_sound(self):
        print("Meow!")

obj1=dog()
obj1.make_sound()
obj2=cat()
obj2.make_sound()