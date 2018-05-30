def dashatize(num):
    try:
        lst = [x for x in str(abs(num))]
    except Exception:
        return "None"
    str1 = ''
    for i in range(len(lst)-1):
        if int(lst[i]) % 2 == 1:
            str1 += lst[i] + '-'
        elif int(lst[i+1]) % 2 ==1:
            str1 += lst[i] + '-'
        else:
            str1 += lst[i]

    str1 += lst[-1]
    print(str1)

dashatize(28369)


import re

def dashatize(num):
  return 'None' if num is None else '-'.join(w for w in re.split(r'([13579])', str(abs(num))) if len(w)>0)

def dashatize(num):
    try:
        return ''.join(['-'+i+'-' if int(i)%2 else i for i in str(abs(num))]).replace('--','-').strip('-')
    except:
        return 'None'