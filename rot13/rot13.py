import string
from codecs import encode as _dont_use_this_

def rot13(message):
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    output = ''

    for this_letter in list(message):
        if this_letter in lowercase:
            output = output + lowercase[(lowercase.index(this_letter) + 13) % 26]
        elif this_letter in uppercase:
            output = output + uppercase[(uppercase.index(this_letter) + 13) % 26]
        else:
            output = output + this_letter

    return output
    pass

