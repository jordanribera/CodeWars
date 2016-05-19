#!/usr/bin/env python
class VigenereCipher(object):

    def __init__(self, key, alphabet):
        self.alphabet = alphabet
        self.key = key
        pass

    def get_offset(self, position):
        key_character = self.key[int(position) % len(self.key)]

        return self.alphabet.index(key_character)

    def encode_character(self, character, position):
        if character not in self.alphabet:
            return character
        offset = self.get_offset(position)
        new_position = (
            (self.alphabet.index(character) + offset) % len(self.alphabet)
        )
        return self.alphabet[new_position]

    def decode_character(self, character, position):
        if character not in self.alphabet:
            return character
        offset = self.get_offset(position)
        new_position = (
            (self.alphabet.index(character) - offset) % len(self.alphabet)
        )
        return self.alphabet[new_position]

    def encode(self, str):
        output = ''
        for position, character in enumerate(str):
            output += self.encode_character(character, position)
        return output

    def decode(self, str):
        output = ''
        for position, character in enumerate(str):
            output += self.decode_character(character, position)
        return output

abc = "abcdefghijklmnopqrstuvwxyz"
key = "password"
c = VigenereCipher(key, abc)

print(c.encode('codewars'))
print(c.decode('rovwsoiv'))
