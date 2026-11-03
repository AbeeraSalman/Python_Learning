
class CustomList:
    def __init__(self):
        self.items = []
        self.size = 0

    def add(self, value):
        self.items.append(value)
        self.size += 1

    def get(self, index):
        try:
            if index < 0 or index >= self.size:
                raise IndexError("Index out of range")

            return self.items[index]

        except IndexError as e:
            print("Error:", e)
            return None

    def remove(self, index):
        try:
            if index < 0 or index >= self.size:
                raise IndexError("Index out of range")

            self.items.pop(index)
            self.size -= 1

        except IndexError as e:
            print("Error:", e)

    def length(self):
        return self.size


object1 = CustomList()

object1.add(1)
object1.add(2)
object1.add(3)

print(object1.get(4))
print(object1.get(2))

object1.remove(3)
object1.remove(1)

print(object1.items)
print("Length:", object1.length())
