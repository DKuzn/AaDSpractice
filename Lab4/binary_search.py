import time
import numpy as np


n = 1
dx = 100000
key = 435


def binary_search(array, key):
    minimum = 0
    maximum = len(array) - 1
    ret = 0
    while minimum <= maximum:
        avg = (maximum + minimum) // 2
        if key < array[avg]:
            maximum = avg - 1
        elif key > array[avg]:
            minimum = avg + 1
        else:
            ret = avg
            break
    while ret > 0 and array[ret - 1] == key:
        ret -= 1
    if array[ret] == key:
        return ret
    else:
        return -1


print('-'*47)
print('{:<1} {:<20} {:<1} {:<20} {:<1}'.format('|', 'Key', '|', 'Time', '|'))
print('-'*47)

while n < 1.0e+6:
    array = np.arange(n, dtype=int)
    a = binary_search(array, key)
    b = time.process_time()
    n += dx
    print('{:<1} {:<20} {:<1} {:<20} {:<1}'.format('|', a, '|', b, '|'))
    print('-' * 47)
