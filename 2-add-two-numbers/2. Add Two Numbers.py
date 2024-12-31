# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        i = l1
        j = l2
        carry = 0

        dummy = ListNode(0,None)
        head = dummy

        while i and j:
            num = (i.val + j.val + carry) % 10
            if (i.val + j.val + carry) >=10:
                carry = 1
            else:
                carry = 0

            dummy.next = ListNode(num, None)
            dummy = dummy.next
        
            i = i.next
            j = j.next
        
        while i:
            num = (i.val  + carry) % 10
            if (i.val  + carry) >=10:
                carry = 1
            else:
                carry = 0

            dummy.next = ListNode(num, None)
            dummy = dummy.next
        
            i = i.next
        while j:
            num = (j.val  + carry) % 10
            if (j.val  + carry) >=10:
                carry = 1
            else:
                carry = 0

            dummy.next = ListNode(num, None)
            dummy = dummy.next
        
            j = j.next

        if carry:
            dummy.next = ListNode(carry, None)
        return head.next

