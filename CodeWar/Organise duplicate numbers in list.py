# def group(arr):
#     lst, lst1 = [], []
#     for i in range(len(arr)):
#         if not arr[i] in lst:
#             lst.append(arr[i])
#             lst1 = lst1 + [[arr[i]]*arr.count(arr[i])]
#     print(lst1)
#
#
# group([3, 2, 6, 2, 1, 3])


group=lambda arr: [[n]*arr.count(n) for n in sorted(set(arr), key=arr.index)]

print(group([3, 2, 6, 2, 1, 3]))
