def decodeMorse(morseCode):
    print(morseCode)
    morseCode = morseCode.strip()
    words = morseCode.split("   ")
    outputWords = []
    output = " "

    for thisWord in words:
        thisOutputWord = ""
        letters = thisWord.split(" ")
        for thisLetter in letters:
            if thisLetter in MORSE_CODE:
                thisOutputWord += MORSE_CODE[thisLetter]
        outputWords.append(thisOutputWord)

    output = output.join(outputWords)

    return output
