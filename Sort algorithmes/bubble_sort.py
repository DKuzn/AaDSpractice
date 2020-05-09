import numpy as np
import time


row = np.random.randint(0, 1000, 100)


def bubble_sort(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


print(row)
bubble_sort(row)
print(row)
print(time.process_time())
