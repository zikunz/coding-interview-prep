# Time Complexity: O(N), where N represents number of nodes in the BST
# Space Complexity: O(1)

def findClosestValueInBst(tree, target):
    currNode = tree
    closest = float('inf')
	
    while currNode is not None:
        if abs(currNode.value - target) < abs(closest - target):
            closest = currNode.value
		
        if target > currNode.value:
            currNode = currNode.right
        elif target < currNode.value:
            currNode = currNode.left
        else:
            break;
			
    return closest

# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
