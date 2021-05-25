# Time Complexity: O(N), where N represents number of elements in array
# Space Complexity: O(N)


def twoNumberSum(array, targetSum):
    nums = set()

    for num in array:
        match = targetSum - num
        if match in nums:
            return [num, match]
        else:
            nums.add(num)

    return []