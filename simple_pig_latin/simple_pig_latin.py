def pig_it(text):
    raw_words = text.split()
    pig_words = [
        pig_word(word)
        for word in raw_words
    ]
    return ' '.join(pig_words)


def pig_word(word):
    first_letter = word[:1]
    remaining_word = word[1:]
    return '{}{}'.format(remaining_word, pig_letter(first_letter))


def pig_letter(letter):
    if letter.isalpha() is False:
        return letter
    return '{}{}'.format(letter, 'ay')
