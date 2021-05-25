# Time Complexity: O(N), where N represents number of elements in array
# Space Complexity: O(1)


def isValidSubsequence(array, sequence):
    seqIdx = 0

    for arrIdx in range(len(array)):
        if array[arrIdx] == sequence[seqIdx]:
            seqIdx += 1
        if seqIdx == len(sequence):
            return True

    return False
