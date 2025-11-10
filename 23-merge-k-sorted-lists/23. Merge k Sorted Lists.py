# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __lt__(self, other):
        return self.val < other.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        class HeapNode:
            def __init__(self, node):
                self.node = node
            def __lt__(self, other):
                return self.node.val < other.node.val

        min_heap = []
        dummy = ListNode(-1)
        curr = dummy

        for head in lists:
            if head:
                heapq.heappush(min_heap, [head.val, HeapNode(head)])
        
        while min_heap:
            val, heap_node = heapq.heappop(min_heap)

            curr.next = heap_node.node
            nextNode = heap_node.node.next
            if nextNode:
                heapq.heappush(min_heap, [nextNode.val, HeapNode(nextNode)])
            curr = curr.next 
        
        return dummy.next