# Time Complexity:
# Worst Case: O(N^2), where N represents the length of the input array
# Best Case: O(N), where N represents the length of the input array
# Space Complexity: O(1)


def bubbleSort(array):
    isSorted = False
    counter = 0

    while not isSorted:
        isSorted = True
        for i in range(0, len(array) - 1 - counter):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                isSorted = False
        counter += 1

    return array