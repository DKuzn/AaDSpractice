import time
import numpy as np


n = 1
dx = 100000
key = 435


def interpolational_search(array, key):
    minimum = 0
    maximum = len(array) - 1
    ret = 0
    while array[minimum] < key < array[maximum]:
        avg = int(minimum + (maximum - minimum) * (key - array[minimum]) / (array[maximum] - array[minimum]))
        if array[avg] == key:
            ret = avg
            break
        elif array[avg] > key:
            maximum = avg - 1
        else:
            minimum = avg + 1

    if array[minimum] == key:
        ret = minimum
    if array[maximum] == key:
        ret = maximum
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
    a = interpolational_search(array, key)
    b = time.process_time()
    n += dx
    print('{:<1} {:<20} {:<1} {:<20} {:<1}'.format('|', a, '|', b, '|'))
    print('-' * 47)
