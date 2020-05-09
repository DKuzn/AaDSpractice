import numpy as np
import time


row = np.random.randint(0, 100, 10)


def shell_sort(array):
    n = len(array)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = array[i]
            j = i
            while j >= gap and array[j - gap] > temp:
                array[j] = array[j - gap]
                j -= gap
            array[j] = temp
        gap //= 2
    return array


print(row)
shell_sort(row)
print(row)
print(time.process_time())
