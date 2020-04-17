def linear_search(array, key):
    for i in range(len(array)):
        if array[i] == key:
            return i


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
    while search > 0 and array[search - 1] == key:
        search -= 1
    if array[search] == key:
        return search
    else:
        return -1


def interpolational_search(array, key):
    minimum = 0
    maximum = len(array) - 1
    search = 0
    while array[minimum] < key < array[maximum]:
        dist = int(minimum + (maximum - minimum) * (key - array[minimum]) / (array[maximum] - array[minimum]))
        if array[dist] == key:
            search = dist
            break
        elif array[dist] > key:
            maximum = dist - 1
        else:
            minimum = dist + 1
    if array[minimum] == key:
        search = minimum
    elif array[maximum] == key:
        search = maximum
    while search > 0 and array[search - 1] == key:
        search -= 1
    if array[search] == key:
        return search
    else:
        return -1


def fibonaccian_search(array, key):
    fib_nm2 = 0
    fib_nm1 = 1
    fib_n = fib_nm2 + fib_nm1
    while fib_n < len(array):
        fib_nm2 = fib_nm1
        fib_nm1 = fib_n
        fib_n = fib_nm2 + fib_nm1
    offset = -1
    while fib_n > 1:
        i = min(offset + fib_nm2, len(array) - 1)
        if array[i] < key:
            fib_n = fib_nm1
            fib_nm1 = fib_nm2
            fib_nm2 = fib_n - fib_nm1
            offset = i
        elif array[i] > key:
            fib_n = fib_nm2
            fib_nm1 = fib_nm1 - fib_nm2
            fib_nm2 = fib_n - fib_nm1
        else:
            return i
    if fib_nm1 and array[offset] == key:
        return offset
    return -1
