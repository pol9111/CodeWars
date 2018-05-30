def series_sum(n):
    if n == 0:
        return '0.00'
    else:
        s = 0
        for i in range(2, n+1):
            s = 1/(3*(i-1)+1) + s
        result = s + 1
        return print('%.2f'%result)


series_sum(1)

#
# def series_sum(n):
#     return '{:.2f}'.format(sum(1.0/(3 * i + 1) for i in range(n)))

# def series_sum(n):
#     return '%.2f' % sum(1.0 / i for i in xrange(1, 3 * n, 3))



