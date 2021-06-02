# Time Complexity: O(N), where N represents the length of elements in string
# Space Complexity: O(N), where N represents the length of elements in string
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