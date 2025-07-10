# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        

        slow = head
        fast = head
        cnt = 1

        while (slow != fast or cnt==1) and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            cnt = 2
        

        if not fast or not fast.next:
            return None
        

        slow = head

        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        return slow

        
