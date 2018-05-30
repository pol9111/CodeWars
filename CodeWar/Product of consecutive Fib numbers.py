def productFib(prod):
    f1 ,f2 = 0, 1
    while f1 * f2 < prod:
        f1, f2 = f2, f1 + f2
    return print([f1, f2, prod == f1 * f2])


productFib(4895)



def productFib(prod, f1=0, f2=1):
    return [f1, f2, True] if prod == f1 * f2 else [f1, f2, False] if prod < f1 * f2 else productFib(prod, f2, f1+f2)


class Fib(object):

    def __init__(self):
        super(Fib, self).__init__()
        self._a = 0
        self._b = 1

    def __call__(self):
        self._a, self._b = self._b, self._a + self._b
        return self._a, self._b


def productFib(prod):
    fib = Fib()
    a, b = fib()
    while (a * b) < prod:
        a, b = fib()
    return [a, b, (a * b) == prod]
