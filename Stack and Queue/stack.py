class MyStack:
    def __init__(self):
        self.data = []

    def __str__(self):
        out = str(self.data)
        return out

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def size(self):
        return len(self.data)


stack = MyStack()
stack.push(2)
stack.push(4)
stack.push(5)
stack.push(7)
print(stack)
print(stack.size())
stack.pop()
print(stack)
print(stack.size())