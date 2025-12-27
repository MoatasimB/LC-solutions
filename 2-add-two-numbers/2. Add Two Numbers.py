# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            digit1 = l1.val if l1 else 0
            digit2 = l2.val if l2 else 0

            digit = digit1 + digit2 + carry

            carry = digit // 10
            digit = digit % 10

            curr.next = ListNode(digit)

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            curr = curr.next
        
        return dummy.next

            