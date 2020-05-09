import random as rd


def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        L = array[:mid]
        R = array[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            array[k] = R[j]
            j += 1
            k += 1
    return array


def array_init(n):
    array = []
    for i in range(n):
        array.append(rd.randint(0, 100))
    return array


arr = array_init(100)
print("Given array is: \n", arr)
merge_sort(arr)
print("Sorted array is: \n", arr)

