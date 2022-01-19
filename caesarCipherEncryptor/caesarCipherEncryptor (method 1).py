# Time Complexity: O(N), where N represents number of elements in string
# Space Complexity: O(N), where N represents number of elements in string

numberOfLetters = 26

def caesarCipherEncryptor(string, key):
    newLetters = []

    for letter in string:
        newLetterCode = ord(letter) + key % numberOfLetters

        if newLetterCode <= ord('z'):
            newLetters.append(chr(newLetterCode))
        else:
            newLetters.append(chr(newLetterCode % ord('z') + ord('a') - 1))

    return ''.join(newLetters)
