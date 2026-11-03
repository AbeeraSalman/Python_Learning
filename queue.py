
class Queue:
    def __init__(self):
        self.items = []


    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return
        return self.items.pop(0)


    def front(self):
        if self.is_empty():
            print("Queue is empty")
            return
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def get_size(self):
        return len(self.items)


queue = Queue()

queue.enqueue(5)
queue.enqueue(6)
queue.enqueue(7)

print(queue.items)
print(queue.front())

queue.dequeue()
print(queue.items)

print(queue.get_size())
