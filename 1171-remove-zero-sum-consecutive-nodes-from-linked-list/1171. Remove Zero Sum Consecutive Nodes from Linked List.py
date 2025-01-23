# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        mpp = {}
        dummy = ListNode(0, head)
        mpp[0] = dummy

        curr = dummy.next
        s = 0

        while curr:
            s += curr.val
            mpp[s] = curr
            curr = curr.next
        
        s = 0
        curr = dummy

        while curr:
            s += curr.val
            curr.next = mpp[s].next
            curr = curr.next
        
        return dummy.next

        


