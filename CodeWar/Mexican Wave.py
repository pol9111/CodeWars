def unique_in_order(iterable):
    # if iterable != []:
        lst = []
        for i, j in enumerate(iterable):
            if int(i) != len(iterable)-1:
                if j != iterable[i+1]:
                    lst.append(j)
            else:
                lst.append(j)

        print(lst)
    # else:
    #     return []

unique_in_order([])
# unique_in_order('AAAABBBCCDAABBB')
# #
# unique_in_order([1,2,2,3,3])

def unique_in_order(iterable):
    res = []
    for item in iterable:
        if len(res) == 0 or item != res[-1]:
            res.append(item)
    return res

unique_in_order('AAAABBBCCDAABBB')
unique_in_order = lambda l: [z for i, z in enumerate(l) if i == 0 or l[i - 1] != z]