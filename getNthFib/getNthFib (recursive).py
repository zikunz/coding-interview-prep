# Time Complexity: O(n)
# Space Complexity: O(n)

def getNthFib(n, memoize = {1: 0, 2: 1}):
    if n not in memoize:
        memoize[n] = getNthFib(n - 1) + getNthFib(n - 2)
		
    return memoize[n]
