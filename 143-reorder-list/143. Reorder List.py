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
        slow = head
        fast = head


        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        if fast == slow:
            return head

        prev = None
        while slow:
            nextNode = slow.next
            slow.next = prev
            prev = slow
            slow = nextNode
        

        first, second = head, prev

        while second.next:
            nextP = second.next
            nextH = first.next

            first.next = second
            first = first.next
            first = nextH
            

            second.next = first
            second = nextP
        
        return head


