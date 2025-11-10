# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        def merge(aHead, bHead):

            dummy = ListNode(-1)
            curr = dummy
            while aHead and bHead:
                if aHead.val < bHead.val:
                    curr.next = aHead
                    aHead = aHead.next
                else:
                    curr.next = bHead
                    bHead = bHead.next
                curr = curr.next
            
            if aHead:
                curr.next = aHead
            if bHead:
                curr.next = bHead
            
            return dummy.next
        

        def mergesort(l, r):
            if l >= r:
                return lists[l]
            
            mid = (l + r) // 2

            left = mergesort(l, mid)
            right = mergesort(mid + 1, r)

            return merge(left, right)
        
        return mergesort(0, len(lists) - 1)
                    