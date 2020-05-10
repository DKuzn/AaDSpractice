class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        if self.head is not None:
            current = self.head
            out = "[" + str(current.data)
            while current.next is not None:
                current = current.next
                out += " " +str(current.data)
            return out + "]"

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def delete_node(self, key):
        temp = self.head
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
            if temp is None:
                return
            prev.next = temp.next
            temp = None


llist = MyLinkedList()

llist.push(1)
llist.push(4)
llist.append(5)
llist.append(10)
print(llist)
llist.append(6)
print(llist)
llist.push(1)
print(llist)