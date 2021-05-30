# Time Complexity: O(N), where N represents number of characters in string
# Space Complexity: O(1)

def isPalindrome(string):
	leftPtr = 0
	rightPtr = len(string) - 1
	
	for leftPtr in range (0, len(string) - 1):
		if string[leftPtr] != string[rightPtr]:
			return False
		rightPtr -= 1
	return True
