# Time Complexity: O(M + N), where M represents the length of characters and N represents the length of document
# Space Complexity: O(C), where C represents number of unique characters in charCounts

def generateDocument(characters, document):
    charCounts = {}
	
    for element in characters:
        if element not in charCounts:
            charCounts[element] = 1
        else:
            charCounts[element] += 1
			
    for element in document:
        if element not in charCounts:
            return False
		
        charCounts[element] -= 1
        if charCounts[element] < 0:
            return False
			
    return True
