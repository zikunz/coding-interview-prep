# Time Complexity: O(N), where N represents number of elements in string
# Space Complexity: O(N), where N represents number of elements in string

def caesarCipherEncryptor(string, key):
    newLetters = []
	
    for letter in string:
        nLC = ord(letter) + key % 26
        if nLC > 122:
            nLC = nLC % 123 + 97
        newLetter = chr(nLC)
        letter = newLetter
        newLetters.append(newLetter)
	
    return "".join(newLetters)
