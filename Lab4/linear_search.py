import time
import numpy as np


n = 1
dx = 100000
key = 435


def linear_search(array, key):

    for i in range(len(array)):
        if array[i] == key:
            return i

    return 0


print('-'*47)
print('{:<1} {:<20} {:<1} {:<20} {:<1}'.format('|', 'Key', '|', 'Time', '|'))
print('-'*47)

while n < 1.0e+6:
    array = np.arange(n, dtype=int).reshape(int(n))
    a = linear_search(array, key)
    b = time.process_time()
    n += dx
    print('{:<1} {:<20} {:<1} {:<20} {:<1}'.format('|', a, '|', b, '|'))
    print('-' * 47)
