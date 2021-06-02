# Time Complexity: O(N), where N represents the length of the input string
# Space Complexity: O(1) as there are only 26 lower-case English letters resulting in the dictionary having no more than 26 keys

def firstNonRepeatingCharacter(string):
    letters = {}

    for letter in string:
        if letter not in letters:
            letters[letter] = 1
        else:
            letters[letter] += 1

    for idx in range(0, len(string)):
        if letters[string[idx]] == 1:
            return idx

    return -1
