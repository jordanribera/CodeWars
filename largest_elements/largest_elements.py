def largest(n,xs):
    xs = sorted(xs)
    while len(xs) > n:
        del xs[0]
    return xs
