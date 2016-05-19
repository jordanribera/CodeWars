def prefill(n, v="undefined"):
    if (n is None) or (representsInt(n) is False):
        raise TypeError(str(n) + ' is invalid')

    if int(n) == 0:
        return []

    output = list()
    n_int = 0
    try:
        n_int = int(n)
    except:
        n_int = 0

    for x in range(0, n_int):
        output.append(v)

    return output


def representsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
