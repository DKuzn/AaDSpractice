class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def get_data(self):
        return self.data

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right


class IterativeBTS:
    def __init__(self, data):
        self.root = Node(data)

    def search(self, key):
        current = self.root
        while current is not None:
            if key == current.get_data():
                return True
            elif key <= current.get_data():
                current = current.get_left()
            else:
                current = current.get_right()
        return False

    def insert(self, key):
        current = self.root
        point = None
        while current is not None:
            point = current
            if key < point.get_data():
                current = current.get_left()
            else:
                current = current.get_right()
        if point is None:
            point = Node(key)
        elif key < point.get_data():
            point.set_left(Node(key))
        else:
            point.set_right(Node(key))
        return point

    def pre_order(self):
        current = self.root
        stack = []
        while True:
            if current is not None:
                stack.append(current)
                print(current.get_data(), end=" ")
                current = current.get_left()
            elif stack:
                current = stack.pop()
                current = current.get_right()
            else:
                break
        print()

    def in_order(self):
        current = self.root
        stack = []
        while True:
            if current is not None:
                stack.append(current)
                current = current.get_left()
            elif stack:
                current = stack.pop()
                print(current.get_data(), end=" ")
                current = current.get_right()
            else:
                break
        print()

    def __peek(self, stack):
        if len(stack) > 0:
            return stack[-1]
        return None

    def post_order(self):
        root = self.root
        ans = []
        stack = []
        while True:
            while root:
                if root.get_right() is not None:
                    stack.append(root.get_right())
                stack.append(root)
                root = root.get_left()
            root = stack.pop()
            if root.get_right is not None and self.__peek(stack) == root.get_right():
                stack.pop()
                stack.append(root)
                root = root.get_right()
            else:
                ans.append(root.get_data())
                root = None
            if len(stack) <= 0:
                break
        for i in range(len(ans)):
            print(ans[i], end=' ')
        print()


bst = IterativeBTS(15)
bst.insert(13)
bst.insert(16)
bst.insert(14)
bst.insert(17)
bst.insert(11)
bst.insert(16)
bst.insert(18)
print('Pre-order:')
bst.pre_order()
print('In-order:')
bst.in_order()
print('Post-order:')
bst.post_order()
print(bst.search(17))


