def calculate_years(principal, interest, tax, desired):
    s = (principal * interest) - (principal * interest * tax) + principal
    if desired == principal:
        return 0
    else:
        years = 1
        while s < desired:
            s = (s * interest) - (s * interest * tax) + s
            years += 1
        return years



calculate_years(1000, 0.05, 0.18, 1100)


def calculate_years(principal, interest, tax, desired):
    years = 0
    while principal < desired:
        principal += (interest * principal) * (1 - tax)
        years += 1
    return years


import math

def calculate_years(principal, interest, tax, desired):
    return 0 if principal >= desired else math.ceil((math.log(desired) - math.log(principal))/math.log(1+interest*(1-tax)))


