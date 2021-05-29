# Time Complexity: O(N), where N represents number of elements in array
# Space Complexity: O(1)


def findThreeLargestNumbers(array):
    threeLargestNums = [None, None, None]

    for num in array:
        if threeLargestNums[2] is None or num > threeLargestNums[2]:
            shiftAndUpdate(threeLargestNums, num, 2)
        elif threeLargestNums[1] is None or num > threeLargestNums[1]:
            shiftAndUpdate(threeLargestNums, num, 1)
        elif threeLargestNums[0] is None or num > threeLargestNums[0]:
            shiftAndUpdate(threeLargestNums, num, 0)

    return threeLargestNums


def shiftAndUpdate(array, num, idx):
    for i in range(idx + 1):
        if i == idx:
            array[i] = num
        else:
            array[i] = array[i + 1]
