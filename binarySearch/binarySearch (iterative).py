# Time Complexity: O(logN), where N represents number of elements in array
# Space Complexity: O(1)

def binarySearch(array, target):
    leftPtr = 0
    rightPtr = len(array) - 1

    while leftPtr <= rightPtr:
        middlePtr = (leftPtr + rightPtr) // 2
        if array[middlePtr] == target:
            return middlePtr
        elif array[middlePtr] > target:
            rightPtr = middlePtr - 1
        else:
            leftPtr = middlePtr + 1

    return -1
