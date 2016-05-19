def make_backronym(acronym):
    acronym = list(acronym)
    output = []
    for letter in acronym:
        output.append(dictionary[letter.upper()])

    return ' '.join(output)
