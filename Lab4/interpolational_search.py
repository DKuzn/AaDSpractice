import time
import numpy as np
import matplotlib.pyplot as plt


def interpolational_search(array, key):
    minimum = 0
    maximum = len(array) - 1
    search = 0
    while array[minimum] < key < array[maximum]:
        dist = int((maximum - minimum) * (key - array[minimum]) / (array[maximum] - array[minimum]))
        if array[dist] == key:
            search = dist
            break
        elif array[dist] > key:
            maximum = dist - 1
        else:
            minimum = dist + 1
    if array[minimum] == key:
        search = minimum
    elif array[maximum] == key:
        search = maximum
    elif array[search] == key:
        return search
    return array[search]


n = 1000
dx = 100000
key = 435
result = []
search_time = []
while n <= 1.0e+6 + 1000:
    array = np.arange(n, dtype=int)
    a = interpolational_search(array, key)
    b = time.process_time()
    n += dx
    result.append(len(array))
    search_time.append(b)

plt.plot(result, search_time, 'g')
plt.ylabel('Time')
plt.xlabel('Array length')
plt.title('Interpolational search')
plt.tight_layout()
plt.grid()
print(result)
print(search_time)

