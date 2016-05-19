def rot13(message):
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                 'y', 'z']
    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
                 'Y', 'Z']

    output = ''

    for letter in list(message):
        if letter in lowercase:
            output = output + lowercase[(lowercase.index(letter) + 13) % 26]
        elif letter in uppercase:
            output = output + uppercase[(uppercase.index(letter) + 13) % 26]
        else:
            output = output + letter

    return output
    pass
