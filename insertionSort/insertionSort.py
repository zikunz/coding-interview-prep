# Time Complexity:
# Worst Case: O(N^2), where N represents the length of the input array
# Best Case: O(N), where N represents the length of the input array

# Space Complexity: O(1) for both best and worst case
def insertionSort(array):
    for currIdx in range(1, len(array)):
        idxDuplicate = currIdx
        while idxDuplicate > 0 and array[idxDuplicate] < array[idxDuplicate - 1]: 
            array[idxDuplicate], array[idxDuplicate - 1] = array[idxDuplicate - 1], array[idxDuplicate]	
            idxDuplicate -= 1
				
    return array
