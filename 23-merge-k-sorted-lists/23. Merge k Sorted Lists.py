# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class HeapNode:
    def __init__(self, node):
        self.node = node
    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        

        minH = []

        for head in lists:
            if head:
                heapNode = HeapNode(head)
                heapq.heappush(minH, heapNode)
        

        dummy = ListNode(-1)

        curr = dummy

        while minH:

            smallestNode = heapq.heappop(minH)

            if smallestNode.node.next:
                heapNode = HeapNode(smallestNode.node.next)
                heapq.heappush(minH, heapNode)

            curr.next = smallestNode.node
            curr = curr.next
        
        return dummy.next