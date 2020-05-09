import numpy as np
import time


row = np.random.randint(0, 100, 10)


def gnome_sort(array):
    for i in range(1, len(array)):
        if array[i - 1] <= array[i]:
            i += 1
        else:
            array[i - 1], array[i] = array[i], array[i - 1]
            if i > 1:
                i -= 1
    return array


print(row)
gnome_sort(row)
print(row)
print(time.process_time())
