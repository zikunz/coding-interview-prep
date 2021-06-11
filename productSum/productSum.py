# Time Complexity: O(N), where N represents total number of elements in array (incl. elements in the subarray(s), if any)
# Space Complexity: O(D), where D represents depth of subarray

def productSum(array, depth = 1):
    pdtSum = 0
	
    for element in array:
        if type(element) is list:
            pdtSum += productSum(element, depth + 1)
        else:
            pdtSum += element
	
    return pdtSum * depth
