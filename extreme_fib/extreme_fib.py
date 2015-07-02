def fib(n):
    print "n: " + str(n)
    abs_n = abs(n)
    a, b = 0, 1
    for i in range(0, abs_n):
        if n < 0:
            a, b = b, a - b
        else:
            a, b = b, a + b
    #print "a: " + str(a)
    return a