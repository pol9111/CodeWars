def high(x):
    dict_alph = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8,
                 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16,
                 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w':23, 'x':24, 'y':25,
                 'z': 26,
    }
    dict_keys = list(dict_alph.keys())

    x_lst = list(x)
    x_lst_split = x.split(' ')

    lst_tmp = []
    lst_get_max = []
    for j in x_lst:
        for i in j:
            if i in dict_keys:
                num = dict_alph.get(i)
                lst_tmp.append(num)
            if i == ' ':
                s = sum(lst_tmp)
                lst_get_max.append(s)
                lst_tmp.clear()
    lst_get_max.append(sum(lst_tmp))
    max_num = max(lst_get_max)
    t = 0
    for i in lst_get_max:
        if max_num == i:
            return print(x_lst_split[t])
        else:
            t += 1



high('man i need a taxi up to ubud')

#BestPractice
def high(words):
    return max(words.split(), key=lambda word: sum(ord(c) - ord('a') + 1 for c in word.lower()))

# def high(x):
#     return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))


