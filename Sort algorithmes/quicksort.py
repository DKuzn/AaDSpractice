import random as rd


def partition(array, low, high):
    i = low - 1
    pivot = array[high]
    for j in range(low, high):
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1


def quick_sort_legacy(array, low, high):
    if low < high:
        part_index = partition(array, low, high)
        quick_sort_legacy(array, low, part_index - 1)
        quick_sort_legacy(array, part_index + 1, high)
    return array


def quick_sort(array):
    quick_sort_legacy(array, 0, len(array) - 1)


def array_init(n):
    array = []
    for i in range(n):
        array.append(rd.randint(0, 100))
    return array


arr = array_init(100)
print("Unsorted array is: \n", arr)
quick_sort(arr)
print("Sorted array is: \n", arr)
