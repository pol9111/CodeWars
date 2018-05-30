def find_uniq(array):
    array_set = list(set(array))
    for i in range(len(array)):
        if array[i] == array[i + 1]:
            array_set.remove(array[i])
            return print(array_set[0])


find_uniq([3, 10, 3, 3, 3])


def find_uniq(arr):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b










