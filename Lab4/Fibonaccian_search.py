import time
import numpy as np
import matplotlib.pyplot as plt


def fibonacci_row(n):
    row = np.zeros(n, dtype=np.int64)
    row[0] = 0
    row[1] = 1
    for i in range(2, n):
        fbr0 = row[i - 1]
        fbr1 = row[i - 2]
        fbr3 = fbr0 + fbr1
        row[i] = fbr3
    return row


def fibonaccian_search(array, key):
    for k in range(len(array) - 1):
        fib = fibonacci_row(len(array))
        i = fib[k]
        p = fib[k - 1]
        q = fib[k - 2]
        while q > 0 and p > 1:
            if key < array[k]:
                i = i - q
                p, q = q, p - q
            elif key > array[k]:
                i = i + q
                p = p - q
                q = q - p
            elif key == array[k]:
                return array[k]


n = 1000
dx = 100000
key = 435
result = []
search_time = []
while n <= 1.0e+6 + 1000:
    array = np.arange(n, dtype=int)
    a = fibonaccian_search(array, key)
    b = time.process_time()
    n += dx
    result.append(len(array))
    search_time.append(b)

plt.plot(result, search_time, 'g')
plt.ylabel('Time')
plt.xlabel('Array length')
plt.title('Linear search')
plt.tight_layout()
plt.grid()
print(result)
print(search_time)
