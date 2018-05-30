def power_sumDigTerm(n):
    lst = []
    for i in range(2,999):
        for j in range(2,15):
            s = 0
            for k in str(i ** j):
                s += int(k)
            if i == int(s):
                lst.append(i ** j)
    lst.sort()
    print(lst)
    return print(lst[n-1])


power_sumDigTerm(33)


def power_sumDigTerm(n):
    lst = []
    for i in range(2, 99):
        for j in range(2, 40):
            s = i ** j
            if i == sum(map(int, str(s))):
                lst.append(s)
    return print(sorted(lst).__getitem__(n))


power_sumDigTerm(3)







