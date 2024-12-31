# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy  = ListNode(-1, None)
        head = dummy
        i = list1
        j = list2

        while i and j:
            if i.val <= j.val:
                dummy.next = i
                dummy = dummy.next
                i = i.next
            else:
                dummy.next = j
                dummy = dummy.next
                j = j.next
        
        if i:
            dummy.next = i
        if j:
            dummy.next = j

        return head.next
        