# def number2words(n):
#     dict = {
#         1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven',
#         8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen',
#         14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen',
#         20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty',
#         90: 'ninety',
#
#     }
#
#     if n < 100:
#         if 1 <= n <= 10:
#             print(dict[n])
#         elif 11 <= n <=19:
#             print(dict[n])
#         elif n % 10 == 0 and n != 0:
#             print(dict[n])
#         elif 21 <= n <= 99:
#             str1 = str(n)
#             print('-'.join([dict[int(str1[-2])*10], dict[int(str1[-1])]]))
#
#     elif 100 <= n < 1000:
#         m = n % 100
#         c = n // 100
#         if n % 100 == 0:
#             str1 = str(n)
#             print(f'{dict[int(str1[-3])]} hundred')
#         elif 1 <= m <= 10:
#             print(' '.join([dict[c], 'hundred', dict[m]]))
#         elif 11 <= m <=19:
#             print(' '.join([dict[c], 'hundred', dict[m]]))
#         elif m % 10 == 0 and m != 0:
#             print(' '.join([dict[c], 'hundred', dict[m]]))
#         elif 21 <= m <= 99:
#             str1 = str(n)
#             result = ('-'.join([dict[int(str1[-2])*10], dict[int(str1[-1])]]))
#             print(' '.join([dict[c], 'hundred', result]))
#
#     elif 1000 <= n < 9999:
#         m = n % 1000 % 100
#         c = n % 1000 // 100
#         t = n // 1000
#         if n % 1000 == 0:
#             str1 = str(n)
#             print(f'{dict[int(str1[-4])]} thousand')
#         if n % 100 == 0:
#             str1 = str(n)
#             print(f'{dict[int(str1[-4])]} thousand {dict[int(str1[-3])]} hundred')
#         elif 1 <= m <= 10:
#             print(' '.join([dict[t], 'thousand', dict[c], 'hundred', dict[m]]))
#         elif 11 <= m <= 19:
#             print(' '.join([dict[t], 'thousand', dict[c], 'hundred', dict[m]]))
#         elif m % 10 == 0 and m != 0:
#             print(' '.join([dict[t], 'thousand', dict[c], 'hundred', dict[m]]))
#         elif 21 <= m <= 99:
#             str1 = str(n)
#             result = ('-'.join([dict[int(str1[-2]) * 10], dict[int(str1[-1])]]))
#             print(' '.join([dict[t], 'thousand', dict[c], 'hundred', result]))
#
#
#
# number2words(2655)
#
# words = "zero one two three four five six seven eight nine" + \
# " ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty" + \
# " thirty forty fifty sixty seventy eighty ninety"
# words = words.split(" ")

words = "zero one two three four five six seven eight nine" + \
" ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty" + \
" thirty forty fifty sixty seventy eighty ninety"
words = words.split(" ")

def number2words(n):
    if n < 20:
        return print(words[n])
    elif n < 100:
        return print([18 + n // 10] + ('' if n % 10 == 0 else '-' + words[n % 10]))
    elif n < 1000:
        return print(number2words(n // 100) + " hundred" + (' ' + number2words(n % 100) if n % 100 > 0 else ''))
    elif n < 1000000:
        return print(number2words(n // 1000) + " thousand" + (' ' + number2words(n % 1000) if n % 1000 > 0 else ''))


number2words(156)
