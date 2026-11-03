class Stack:
    def __init__(self):
        self.items=[]
    def push(self,value):
        self.items.append(value)
    def pop(self):
        if self.is_empty():
            print("Stack is empty")
            return
        else:
            self.items.pop()
    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return
        else:
            return self.items[-1]

    def get_size(self):
        return len(self.items)
    def is_empty(self):
        return self.items == []

stack=Stack()
stack.push(5)
stack.push(6)
stack.push(7)
print(stack.peek())
stack.pop()
print(stack.peek())
print(stack.get_size())
