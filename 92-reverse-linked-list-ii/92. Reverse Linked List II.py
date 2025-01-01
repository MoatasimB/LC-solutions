# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        prev = ListNode(0, head)
        dummy = ListNode(-600, head)
        slow = head
        fast = head
        
        for _ in range(left - 1):
            prev = prev.next
            slow = slow.next
        for _ in range(right - 1):
            fast = fast.next

        end = fast.next
        beginning = slow
        
        prev.next = fast
        p = end
        while slow != end:
            nextNode = slow.next
            slow.next = p
            p = slow
            slow = nextNode
        
        # # prev.next = fast
        # beginning.next = slow
        
        if left == 1:
            return p

        return dummy.next