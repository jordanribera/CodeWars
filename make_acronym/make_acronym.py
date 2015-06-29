def make_acronym(phrase):
    output = ""
    if isinstance(phrase, basestring):
        for word in phrase.split():
            if word.isalpha():
                output = output + word[:1]
            else:
                return "Not letters"
    else:
        return "Not a string"
    return output.upper()
