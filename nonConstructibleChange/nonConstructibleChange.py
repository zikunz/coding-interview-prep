# Time Complexity: O(NlogN), where N represents number of elements in coins
# Space Complexity: O(1) if in place and O(N) if not in place


def nonConstructibleChange(coins):
    coins.sort()
    currMaxAmountOfChange = 0

    for coin in coins:
        if coin > currMaxAmountOfChange + 1:
            return currMaxAmountOfChange + 1
        currMaxAmountOfChange += coin

    return currMaxAmountOfChange + 1