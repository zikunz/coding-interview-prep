# Time Complexity: O(N), where N represents number of elements in array
# Space Complexity: O(N), where N represents number of elements in array

def sortedSquaredArray(array):
    sortedSquaredArray = [0 for _ in array]

    smallerValueIdx = 0
    largerValueIdx = len(array) - 1
    sortedSquaredArrayIdx = len(array) - 1

    while smallerValueIdx <= largerValueIdx:
        if array[smallerValueIdx] ** 2 >= array[largerValueIdx] ** 2:
            sortedSquaredArray[sortedSquaredArrayIdx] = array[smallerValueIdx] ** 2
            sortedSquaredArrayIdx -= 1
            smallerValueIdx += 1
        else:
            sortedSquaredArray[sortedSquaredArrayIdx] = array[largerValueIdx] ** 2
            sortedSquaredArrayIdx -= 1
            largerValueIdx -= 1

    return sortedSquaredArray
