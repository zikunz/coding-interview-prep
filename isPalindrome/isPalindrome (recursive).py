# Time Complexity: O(N), where N represents number of characters in string
# Space Complexity: O(N) (adding frames to the call stack due to recursive calls uses extra memory)

def isPalindrome(string):
	return isPalindromeHelper(string, 0, len(string) - 1)
	
def isPalindromeHelper(array, leftPtr, rightPtr):
	if leftPtr >= rightPtr:
		return True
	
	if array[leftPtr] != array[rightPtr]:
		return False
		
	return isPalindromeHelper(array, leftPtr + 1, rightPtr - 1)	
