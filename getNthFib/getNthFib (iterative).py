# Time Complexity: O(n)
# Space Complexity: O(1)

def getNthFib(n):
    twoLatestNums = [0, 1]
    count = 2
	
    while count < n:
        nextFib = twoLatestNums[0] + twoLatestNums[1]
        twoLatestNums[0] = twoLatestNums[1]
        twoLatestNums[1] = nextFib
        count += 1

    return twoLatestNums[1] if n > 1 else twoLatestNums[0]
