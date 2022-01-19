# Time Complexity: O(N), where N represents number of nodes in the BST
# Space Complexity: O(N), where N represents number of nodes in the BST (adding frames to the call stack due to recursive calls using extra memory)

def findClosestValueInBst(tree, target):
    return findClosestValueInBstHelper(tree, target, float('inf'))

def findClosestValueInBstHelper(tree, target, closest):
    if tree is None:
        return closest
	
    if abs(tree.value - target) < abs(closest - target):
        closest = tree.value
	
    if target > tree.value:
        return findClosestValueInBstHelper(tree.right, target, closest)
    elif target < tree.value:
        return findClosestValueInBstHelper(tree.left, target, closest)
    else:
        return closest
	
# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
