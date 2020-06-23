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

    def __subtree_search(self, value):
        if value < self.root and self.left:
            return self.left.__subtree_search(value)
        elif value > self.root and self.right:
            return self.right.__subtree_search(value)
        if value == self.root:
            return self

    def __clear_node(self):
        self.root = None
        self.left = None
        self.right = None

    def __find_minimum_value(self):
        if self.left:
            return self.left.__find_minimum_value()
        else:
            return self.root

    def delete_node(self, value, parent):
        if value < self.root and self.left:
            return self.left.delete_node(value, self)
        elif value < self.root:
            return False
        elif value > self.root and self.right:
            return self.right.delete_node(value, self)
        elif value > self.root:
            return False
        else:
            if self.left is None and self.right is None and self == parent.left:
                parent.left = None
                self.__clear_node()
            elif self.left is None and self.right is None and self == parent.right:
                parent.right = None
                self.__clear_node()
            elif self.left and self.right is None and self == parent.left:
                parent.left = self.left
                self.__clear_node()
            elif self.left and self.right is None and self == parent.right:
                parent.right = self.left
                self.__clear_node()
            elif self.left is None and self.right and self == parent.left:
                parent.left = self.right
                self.__clear_node()
            elif self.left is None and self.right and self == parent.right:
                parent.right = self.right
                self.__clear_node()
            else:
                self.root = self.right.__find_minimum_value()
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

    def __in_order(self, array):
        if self.left:
            self.left.__in_order(array)
        array.append(self.root)
        if self.right:
            self.right.__in_order(array)

    def post_order(self):
        if self.left:
            self.left.post_order()
        if self.right:
            self.right.post_order()
        print(self.root, end=" ")

    def sequence_less_key(self, key):
        keys = []
        out = []
        self.__in_order(keys)
        for i in range(len(keys)):
            if keys[i] < key:
                out.append(keys[i])
            else:
                break
        print(out)

    def __subtrees_sizes(self, root):
        left = []
        right = []
        found = self.__subtree_search(root)
        if found.left:
            found.left.__in_order(left)
        elif found.right:
            found.right.__in_order(right)
        return len(left) == len(right)

    def sub_trees_compare(self):
        keys = []
        nodes = []
        self.__in_order(keys)
        for i in range(len(keys)):
            root = keys[i]
            compare = self.__subtrees_sizes(root)
            if compare:
                nodes.append(root)
        print(nodes)
