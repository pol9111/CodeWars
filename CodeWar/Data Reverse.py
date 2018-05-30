# def data_reverse(data):
#     data_len = len(data)
#     data_bit = data_len / 8
#     data_rev = []
#     for j in range(int(data_bit)):
#         t = -8
#         for i in range(8):
#             data_rev.append(data[t])
#             data.pop(t)
#             t += 1
#     print(data_rev)
#
#
#
# data_reverse([11,11,1,1,0,1,1,0,0,0,1,0,1,0,0,1])
# # data_reverse([1,2,1,0,5,6,7,8,11,22,33,0,1,66,77,88])
# # data_reverse([1,2,3,4,5,6,7,8,11,22,33,44,55,66,77,88])



def dat_reverse(data):
    return print([b for a in range(len(data)-8,-1,-8) for b in data[a:a+8]])


dat_reverse([11,11,1,1,0,1,1,0,0,0,1,0,1,0,0,1])





