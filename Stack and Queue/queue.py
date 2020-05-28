class MyQueue:
    def __init__(self):
        self.data = []
        self.empty = True

    def __str__(self):
        out = str(self.data)
        return out

    def push(self, item):
        self.data.insert(0, item)
        if self.empty:
            self.empty = False

    def pop(self):
        self.data.pop()
        if not self.data:
            self.empty = True

    def check_empty(self):
        if self.empty:
            return True
        else:
            return False

    def size(self):
        return len(self.data)
