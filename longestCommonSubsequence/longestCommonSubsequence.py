# Time Complexity: O(NM) where N and M refer to the length of str1 and str2 respectively
# Space Complexity: O(NM) where N and M refer to the length of str1 and str2 respectively

def longestCommonSubsequence(str1, str2):
    # Create a 2D array of size N * M where each entry contains a letter (can be "") to be added to LCS,
    # length of the current LCS and i and j index of the previous letter in LCS
    lcs_arr = [[[None, 0, None, None]
                for x in range(len(str1) + 1)] for y in range(len(str2) + 1)]

    for i in range(1, len(str2) + 1):
        for j in range(1, len(str1) + 1):
            if str2[i - 1] == str1[j - 1]:
                lcs_arr[i][j] = [str2[i - 1], lcs_arr[i - 1]
                                 [j - 1][1] + 1, i - 1, j - 1]
            # If left has longer LCS than above
            elif str2[i - 1] != str1[j - 1] and lcs_arr[i - 1][j][1] > lcs_arr[i][j - 1][1]:
                lcs_arr[i][j] = [None, lcs_arr[i - 1][j][1], i - 1, j]
            else:  # We can arbitrarily pick a LCS if length of LCS from the left is the same as that from above, here, we just pick the LCS from the left
                lcs_arr[i][j] = [None, lcs_arr[i][j - 1][1], i, j - 1]

    return buildSequence(lcs_arr)


def buildSequence(lcs_arr):
    lcs = []
    i = len(lcs_arr) - 1  # i index of the last entry
    j = len(lcs_arr[0]) - 1  # j index of the last entry

    while i != 0 and j != 0:
        current_entry = lcs_arr[i][j]
        if current_entry[0] is not None:
            lcs.append(current_entry[0])
        i = current_entry[2]
        j = current_entry[3]

    return list(reversed(lcs))
