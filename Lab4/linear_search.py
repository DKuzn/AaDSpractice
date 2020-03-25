import time
import numpy as np


n = 1000
dx = 100000
key = 435


def linear_search(array, key):
    for i in range(len(array)):
        if array[i] == key:
            return array[i]


print('-'*47)
print('{:<1} {:<20} {:<1} {:<20} {:<1}'.format('|', 'Key', '|', 'Time', '|'))
print('-'*47)

while n < 1.0e+6:
    array = np.arange(n, dtype=int)
    a = linear_search(array, key)
    b = time.process_time()
    n += dx
    print('{:<1} {:<20} {:<1} {:<20} {:<1}'.format('|', a, '|', b, '|'))
    print('-' * 47)
