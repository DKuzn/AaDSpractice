import time
import numpy as np


n = 1
dx = 10
key = 43


def binary_search(array, key):
    minimum = 0
    maximum = len(array) - 1
    search = 0
    while minimum <= maximum:
        avg = (maximum + minimum) // 2
        if key < array[avg]:
            maximum = avg - 1
        elif key > array[avg]:
            minimum = avg + 1
        else:
            search = avg
            break
    if array[search] == key:
        search = array[search]
        return search
    else:
        return -1

def hubble_sort(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


print('-'*47)
print('{:<1} {:<20} {:<1} {:<20} {:<1}'.format('|', 'Key', '|', 'Time', '|'))
print('-'*47)

array = np.random.randint(0, 100, 25)
hubble_sort(array)
print(array)
a = binary_search(array, key)
print(a)
#while n < 1000:
    #array = np.random.randint(0, 1000, n)
    #hubble_sort(array)
    #b = binary_search(array, key)
    #c = time.process_time()
    #n += dx
    #print('{:<1} {:<20} {:<1} {:<20} {:<1}'.format('|', b, '|', c, '|'))
    #print('-' * 47)
