def order(sentence):
    array = sentence.split()

    toReturn = ""

    new_dict = {"1": "NONE", "2": "NONE", "3": "NONE", "4": "NONE", "5": "NONE", "6": "NONE", "7": "NONE", "8": "NONE",
               "9": "NONE", }
#BestPlace1
    for word in array:
        for char in word:
            if char.isdigit() and int(char) <= 9:
                new_dict[char] = word

    sorted_dict = sorted(new_dict.items())
    print(sorted_dict)
#BestPlace2
    for s in sorted_dict:
        if s[1] != 'NONE':
            toReturn = toReturn + s[1] + ' '

    print(toReturn)
    toReturn1 = toReturn[:-1]
    return print(toReturn1)

order("is2 Thi1s T4est 3a")


def order(s):
    z = []
    for i in range(1,10):
        for j in list(s.split()):
        #BestPlace
            if str(i) in j:
               z.append(j)
    return print(" ".join(z))
