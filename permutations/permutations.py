import itertools
def permutations(string):
    perms = set([''.join(p) for p in itertools.permutations(string)])
    return perms