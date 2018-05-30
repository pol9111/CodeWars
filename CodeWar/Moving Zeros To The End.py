def move_zeros(array):
    num = array.count(0)
    print(num)
    for i in array:
        if not isinstance(i, bool) and i != 0:
            array.remove(0)
            array.append(0)

    print(array)


move_zeros([1, 2, False, 0, 1, 0, 3, [], 0, 1, 9, 0, 0, {}, 0, 0, 9])
#
# def move_zeros(array):
#     zeros, arr = [], []
#     for number in array:
#         if not isinstance(number, bool) and number == 0:
#             zeros.append(0)
#         else:
#             arr.append(number)
#     return arr + zeros
#
def move_zeros(arr):
    l = [i for i in arr if isinstance(i, bool) or i!=0]
    return l+[0]*(len(arr)-len(l))
#
# def move_zeros(array):
#     return sorted(array, key=lambda x: x==0 and type(x) is not bool)
