class MyBinarySearchTree:
    def __init__(self, data):
        self.root = data
        self.left = None
        self.right = None

    def insert(self, data):
        if data <= self.root and self.left:
            self.left.insert(data)
        elif data <= self.root:
            self.left = MyBinarySearchTree(data)
        elif data > self.root and self.right:
            self.right.insert(data)
        else:
            self.right = MyBinarySearchTree(data)

    def search(self, value):
        if value < self.root and self.left:
            return self.left.search(value)
        elif value > self.root and self.right:
            return self.right.search(value)
        return value == self.root

    def clear_node(self):
        self.root = None
        self.left = None
        self.right = None

    def find_minimum_value(self):
        if self.left:
            return self.left.find_minimum_value()
        else:
            return self.root

    def delete_node(self, value, parent):
        if value < self.root and self.left:
            return self.left.delete_node(value, parent)
        elif value < self.root:
            return False
        elif value > self.root and self.right:
            return self.right.delete_node(value, parent)
        elif value > self.root:
            return False
        else:
            if self.left is None and self.right is None and self == parent.left:
                parent.left = None
                self.clear_node()
            elif self.left is None and self.right is None and self == parent.right:
                parent.right = None
                self.clear_node()
            elif self.left and self.right is None and self == parent.left:
                parent.left = self.left
                self.clear_node()
            elif self.left and self.right is None and self == parent.right:
                parent.right = self.left
                self.clear_node()
            elif self.left is None and self.right and self == parent.left:
                parent.left = self.right
                self.clear_node()
            elif self.left is None and self.right and self == parent.right:
                parent.right = self.right
                self.clear_node()
            else:
                self.root = self.right.find_minimum_value()
                self.right.delete_node(self.root, self)
            return True

    def pre_order(self):
        print(self.root, end=" ")
        if self.left:
            self.left.pre_order()
        if self.right:
            self.right.pre_order()

    def in_order(self):
        if self.left:
            self.left.in_order()
        print(self.root, end=" ")
        if self.right:
            self.right.in_order()

    def post_order(self):
        if self.left:
            self.left.post_order()
        if self.right:
            self.right.post_order()
        print(self.root, end=" ")


bst = MyBinarySearchTree(20)
bst.insert(15)
bst.insert(17)
bst.insert(21)
bst.insert(19)
bst.insert(25)
bst.insert(27)
bst.insert(13)
print(bst.search(15))
print("Pre-order:")
bst.pre_order()
print("\nIn-order:")
bst.in_order()
print("\nPost-order:")
bst.post_order()