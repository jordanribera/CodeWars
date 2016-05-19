def fib(n):
    abs_n = abs(n)
    if n < 0 and (n % 2 == 0):
        return 0 - bigfib(abs_n)[0]
    return bigfib(abs_n)[0]


def bigfib(n):
    if n == 0:
        return (0, 1)
    else:
        a, b = bigfib(n // 2)
        c = a * (b * 2 - a)
        d = a * a + b * b
        if n % 2 == 0:
            return (c, d)
        else:
            return (d, c + d)
