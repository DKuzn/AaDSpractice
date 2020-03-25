import numpy as np


def fibonacci_row(n):
    row = np.zeros(n, dtype=int)
    row[0] = 0
    row[1] = 1
    for i in range(2, n):
        fbr0 = row[i - 1]
        fbr1 = row[i - 2]
        fbr3 = fbr0 + fbr1
        row[i] = fbr3
    return row


def fibonacci_search(array, key):
    for k in range(len(array) - 1):
        fib = fibonacci_row(len(array))
        i = fib[k]
        p = fib[k - 1]
        q = fib[k - 2]
        while q >= 0 and p >= 1:
            if key < array[k]:
                i = i - q
                p, q = q, p - q
            elif key > array[k]:
                i = i + q
                p = p - q
                q = q - p
            elif key == array[k]:
                return array[k]


key = 11
arr = np.arange(25, dtype=int)
a = fibonacci_search(arr, key)
print(a)
