class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next


class MyLinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        if self.head is not None:
            current = self.head
            out = "[" + str(current.get_data())
            while current.get_next() is not None:
                current = current.get_next()
                out += "," + " " + str(current.get_data())
            return out + "]"

    def push(self, value):
        temp = Node(value)
        temp.set_next(self.head)
        self.head = temp

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.get_next()
        last.set_next(new_node)

    def insert_after(self, key, new_data):
        current = self.head
        found = False
        while current is not None and not found:
            if current.get_data() == key:
                found = True
            else:
                current = current.get_next()
        if found:
            new_node = Node(new_data)
            new_node.set_next(current.get_next())
            current.set_next(new_node)

    def length(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()
        return count

    def search(self, key):
        current = self.head
        found = False
        while current is not None and not found:
            if current.get_data() == key:
                found = True
            else :
                current = current.get_next()
        return found

    def delete_node(self, key):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == key:
                found = True
            else:
                previous = current
                current = current.get_next()
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())


llist = MyLinkedList()

llist.push(1)
llist.push(4)
llist.push(6)
print(llist)
llist.delete_node(4)
print(llist)
llist.append(7)
llist.append(8)
print(llist)
llist.push(1)
print(llist)
print(llist.length())
print(llist.search(6))
llist.insert_after(6, 9)
print(llist)
print(llist.length())
