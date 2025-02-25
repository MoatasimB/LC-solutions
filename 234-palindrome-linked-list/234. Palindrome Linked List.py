# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        dummy = ListNode(-1, head)
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
    #     if fast:
    #         slow = slow.next
  
    # 1 2 3 2 1
    #     s.   f

        prev = None
        while slow:
            nextNode = slow.next
            slow.next = prev
            prev = slow
            slow = nextNode
        
        while prev:
            if prev.val != head.val:
                return False
            head = head.next
            prev = prev.next
        
        return True

        