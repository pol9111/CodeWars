def alphabet_position(text):
    lst = []
    for i in text.lower():
        if i.isalpha():
            result = str(ord(i) - ord('a') + 1)
            lst.append(result)
    result_str = ' '.join(lst)
    print(result_str)
#
# def alphabet_position(text):
#     operation = lambda word: [str((ord(c) - ord('a') + 1)) for c in word.lower() if c.isalpha()]
#     result = ' '.join(operation(text))
#     print(result)
#
# alphabet_position("The sunset sets at twelve o' clock.")
#
# #
# def alphabet_position(text):
#     operation = lambda word: ' '.join([str((ord(c) - ord('a') + 1)) for c in word.lower() if c.isalpha()])
#     print(operation(text))
#
# alphabet_position("The sunset sets at twelve o' clock.")

def alphabet_position(text):
    print(' '.join(str(ord(c) - ord('a') + 1) for c in text.lower() if c.isalpha()))

alphabet_position("The sunset sets at twelve o' clock.")

alphabet_position = lambda text:' '.join(str(ord(c) - ord('a') + 1) for c in text.lower() if c.isalpha())


