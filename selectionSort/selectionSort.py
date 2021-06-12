# Time Complexity:
# Worst Case: O(N^2), where N represents the length of the input array
# Best Case: O(N^2), where N represents the length of the input array

# Space Complexity: O(1) for both best and worst case
def selectionSort(array):
    for idx in range(0, len(array) - 1):
        smallestValIdx = idx
        for nextIdx in range(idx + 1, len(array)):
            if array[nextIdx] < array[smallestValIdx]:
                smallestValIdx = nextIdx
        array[idx], array[smallestValIdx] = array[smallestValIdx], array[idx]	
		
    return array
