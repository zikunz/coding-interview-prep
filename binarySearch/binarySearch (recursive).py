# Time Complexity: O(logN), where N represents number of elements in array
# Space Complexity: O(logN) (adding frames to the call stack due to recursive calls uses extra memory)

def binarySearch(array, target):
    return binarySearchHelper(array, target, 0, len(array) - 1)

def binarySearchHelper(array, target, leftPtr, rightPtr):
    if leftPtr > rightPtr:
        return -1

    middlePtr = (leftPtr + rightPtr) // 2

    if array[middlePtr] == target:
        return middlePtr
    elif array[middlePtr] > target:
        return binarySearchHelper(array, target, leftPtr, middlePtr - 1)
    else:
        return binarySearchHelper(array, target, middlePtr + 1, rightPtr)
