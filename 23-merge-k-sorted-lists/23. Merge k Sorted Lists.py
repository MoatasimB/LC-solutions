# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        def merge(lHead, rHead):
            dummy = ListNode(-1)
            
            curr = dummy
            
            while lHead and rHead:
                if lHead.val < rHead.val:
                    curr.next = lHead
                    lHead = lHead.next
                else:
                    curr.next = rHead
                    rHead = rHead.next
                
                curr = curr.next
            
            if lHead:
                curr.next = lHead
            
            if rHead:
                curr.next = rHead
            
            return dummy.next
            
                    
                    
        
        def mergeSort(l, r):
            if l >= r:
                return lists[l]
            
            mid = (l + r) // 2
            
            left = mergeSort(l, mid)
            right = mergeSort(mid + 1, r)
            
            return merge(left, right)
        
        
        return mergeSort(0, len(lists) - 1)
        
        
        
        
        