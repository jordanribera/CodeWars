ALPHABET = 'abcdefghijklmnopqrstuvwxyz'


def high(x):
    highest_score = 0
    highest_word = ''
    for w in x.split():
        if word_score(w) > highest_score:
            highest_score = word_score(w)
            highest_word = w
    return highest_word


def word_score(w):
    return sum([(ALPHABET.find(c) + 1) for c in list(w)])
