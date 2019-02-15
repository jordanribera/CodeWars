def namelist(names):
    names = [n['name'] for n in names]
    if len(names) >= 2:
        joined = ' & '.join(names[-2:])
        del names[-2:]
        names.append(joined)
    return ', '.join(names)
