from Linked_list.linked_list import MyLinkedList
import random as rd

polynomial = MyLinkedList()
test = MyLinkedList()


def polynom(x, n):
    for i in range(n, -1, -1):
        p = rd.randint(0, 10) * x ** i
        if p != 0:
            polynomial.append(p)
    return polynomial


print(polynom(2, 10))
