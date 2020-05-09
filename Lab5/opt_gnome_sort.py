import numpy as np
import time


row = np.random.randint(0, 100, 10)


def opt_gnome_sort(array):
    i, j, size = 1, 2, len(array)
    while i < size:
        if array[i - 1] <= array[i]:
            i, j = j, j + 1
        else:
            array[i - 1], array[i] = array[i], array[i - 1]
            i -= 1
            if i == 0:
                i, j = j, j + 1
    return array


print(row)
opt_gnome_sort(row)
print(row)
print(time.process_time())