# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        slow = head
        dummy = ListNode(0, head)
        prev = dummy

        for _ in range(n):
            fast = fast.next
        
        while fast:
            fast = fast.next
            slow = slow.next
            prev = prev.next
        
        prev.next = slow.next

        return dummy.next