import numpy as np
import time


row = np.random.randint(0, 100, 10)


def shaker_sort(array):
    up = range(len(array) - 1)
    while True:
        for indices in (up, reversed(up)):
            swapped = False
            for i in indices:
                if array[i] > array[i + 1]:
                    array[i], array[i + 1] = array[i + 1], array[i]
                    swapped = True
        if not swapped:
            return array


print(row)
shaker_sort(row)
print(row)
print(time.process_time())