import re


def is_valid_IP(string):
    str1 = string.split('.')
    if re.findall('[a-z]',string):
        return print('F')
    elif len(str1) != 4 or re.findall(' ',string):
        return print('F')
    else:

        for i in str1:
            if int(i) > 255 or int(i) < 0:
                return print('F')
        return print('T')


is_valid_IP('12.34.56 .1')


def is_valid_IP(strng):
  lst = strng.split('.')
  passed = 0
  for sect in lst:
    if sect.isdigit():
      if sect[0] != '0':
        if 0 < int(sect) <= 255:
          passed += 1
  return passed == 4
#Add a counter to see if it has been recycled four times. if no return False or return True.
#'56  '.isdigit() to see if it's a number.  False
#lst  sect[0] check the first number.




import re
def is_valid_IP(strng):
    return bool(re.match(r'^((\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])(\.(?!$)|$)){4}(?=$)',strng))