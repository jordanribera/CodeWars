import string


class CaesarCipher(object):
    alphabet = string.ascii_uppercase

    def __init__(self, shift):
        self.shift = shift

    def shift_char(self, char, reverse=False):
        if char in self.alphabet:
            shift_by = self.shift
            if reverse:
                shift_by = 0 - self.shift
            return self.alphabet[(
                self.alphabet.index(char) + shift_by
            ) % len(self.alphabet)]

        return char

    def encode(self, str):
        print(str)
        return ''.join([
            self.shift_char(char)
            for char in str.upper()
        ])

    def decode(self, str):
        return ''.join([
            self.shift_char(char, reverse=True)
            for char in str.upper()
        ])
