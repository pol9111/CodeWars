# def divisors(integer):
#     li1 = []
#     for i in range(2, int(integer)):
#         if int(integer) % i == 0:
#             result = int(integer) // i
#             li1.append(result)
#     if li1:
#         li1.sort()
#         print(li1)
#     else:
#         print(f"({integer}) is prime.")
#
#
# while True:
#     input1 = input("Enter a integer:")
#     divisors(input1)




# def divisors(num):
#     l = [a for a in range(2,num) if num%a == 0]
#     if len(l) == 0:
#         return str(num) + " is prime"
#     return l
#
#
#
def divisors(n):
    return print([i for i in range(2, n) if not n % i] or '%d is prime' % n)


divisors(12)






