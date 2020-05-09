import numpy as np
import time


row = np.random.randint(0, 1000, 100)


def insertion_sort(array):
    for i in range(len(array)):
        j = i - 1
        key = array[i]
        while array[j] > key and j >= 0:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array


print(row)
insertion_sort(row)
print(row)
print(time.process_time())

