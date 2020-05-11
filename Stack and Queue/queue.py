class Queue:
    def __init__(self):
        self.data = []

    def __str__(self):
        current = self.data
        out = str(current)
        return out

    def push(self, item):
        self.data.insert(0, item)

    def remove(self):
        return self.data.pop()

    def size(self):
        return len(self.data)


queue = Queue()
queue.push(1)
queue.push(3)
queue.push(2)
queue.push(4)
print(queue)
print(queue.size())
queue.remove()
print(queue)
print(queue.size())
