import numpy as np
import time


row = np.random.randint(0, 1000, 100)


def selection_sort(array):
    for i in range(len(array) - 1):
        m = i
        j = i + 1
        while j < len(array):
            if array[j] < array[m]:
                m = j
            j += 1
        array[i], array[m] = array[m], array[i]


print(row)
selection_sort(row)
print(row)
print(time.process_time())
