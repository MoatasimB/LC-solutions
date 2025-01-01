# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head
        

        
        dummy = ListNode(0, head)
        slow = head
        fast = head.next
        prev = dummy

        while fast:
            if fast.val == slow.val:
                while fast and fast.val == slow.val:
                    fast = fast.next
                    slow = slow.next
                prev.next  = fast
                
            else:
                prev = prev.next
            if fast:
                fast = fast.next
                slow = slow.next
        
        return dummy.next
