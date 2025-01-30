# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        dummy = ListNode(-1, head)

        slow = dummy
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        if fast == head:
            return head
        start = slow.next
        slow.next = None
        prev = None

        while start:
            nextNode = start.next
            start.next = prev
            prev = start
            start = nextNode

        start = head


        while start and prev:
            nextNode = start.next
            nextPrev = prev.next
            start.next = prev
            if not nextNode:
                break
            prev.next = nextNode
            prev = nextPrev
            start = nextNode
        
        return dummy.next