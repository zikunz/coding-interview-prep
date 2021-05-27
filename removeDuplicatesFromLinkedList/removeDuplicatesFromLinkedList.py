# Time Complexity: O(N), where N represents number of elements in linkedList
# Space Complexity: O(1)

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def removeDuplicatesFromLinkedList(linkedList):
    currNode = linkedList

    while currNode is not None:
        nextDiffNode = currNode.next
        while nextDiffNode is not None and nextDiffNode.value == currNode.value:
            nextDiffNode = nextDiffNode.next
        currNode.next = nextDiffNode
        currNode = nextDiffNode

    return linkedList
