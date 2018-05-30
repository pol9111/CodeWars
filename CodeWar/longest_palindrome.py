def longest_palindrome(s):
    pal_length = 0
    for i in range(len(s)):
        for j in range(len(s)-i+1):
            sub_s = s[i:i+j]

            if sub_s == sub_s[::-1] and len(sub_s) > pal_length:
                pal_length = len(sub_s)

    return print(pal_length)



longest_palindrome ("12321aaaaaa")

# def longest_palindrome (s):
#     longest = 0
#     for left in range(len(s)):
#         for right in range(len(s), left, -1):
#             if s[left:right] in (s[left:right])[::-1]:
#                 longest = max(right-left, longest)
#                 break
#     return longest






