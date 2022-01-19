# Time Complexity: O(N), where N represents number of elements in string
# Space Complexity: O(N), where N represents number of elements in string

numberOfLetters = 26

def caesarCipherEncryptor(string, key):
    newLetters = []
    alphabet = list('abcdefghijklmnopqrstuvwxyz')

    for letter in string:
        newLetters.append(findNewLetter(letter, alphabet, key))

    return ''.join(newLetters)

def findNewLetter(letter, alphabet, key):
    index = (alphabet.index(letter) + key) % numberOfLetters  # between 0 and 25

    return alphabet[index]
