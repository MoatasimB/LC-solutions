# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0)
        prev = dummy


        while head and head.next:
            if head.val == head.next.val:
                j = head
                while j and j.val == head.val:
                    j = j.next
                head = j
                continue

            prev.next = head
            prev = head
            head = head.next

        if head:
            prev.next = head
            prev = head
            head = head.next
        else:
            prev.next = None
        
        return dummy.next
        