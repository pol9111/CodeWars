# import re
#
# def domain_name(url):
#     do_na = re.findall(r'http?://+\w', url)
#     a = ''.join(do_na)
#     do_na1 = a.strip('.com')
#     print(do_na1)
#
#
# domain_name("https://www.zombie-bites.com")


# def domain_name(url):
#     return print(url.split("//")[-1].split("www.")[-1].split(".")[0])
#
#
#
# domain_name("https://www.zombie-bites.com")


import re


def domain_name(url):
    return print(re.search('(https?://)?(www\d?\.)?(?P<name>[\w-]+)\.', url).group('name'))


domain_name("https://www.zombie-bites.com")