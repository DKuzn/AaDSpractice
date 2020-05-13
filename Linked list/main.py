from .linked_list import MyLinkedList


polynomial = MyLinkedList()


def polynom(x, n, a):
    for i in range(n, n):
        p = a * x ** n
        if p != 0:
            polynomial.append(p)
    return polynomial


polynom = polynom(2, 10, 5)
print(polynom)