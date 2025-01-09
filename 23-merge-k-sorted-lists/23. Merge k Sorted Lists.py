# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def merge(l1, l2):
            dummy = ListNode(-1)
            curr = dummy
            while l1 and l2:
                # print(l1.val, l2.val)
                if l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                # print(curr.val)
                curr = curr.next
            curr.next = l1 if l1 else l2
            curr = dummy
            while curr:
                curr = curr.next
            return dummy.next
        
        def mergeS(left, right):
            if left >=right:
                return lists[left]
            
            mid = (left + right) // 2

            l1 = mergeS(left, mid)
            l2 = mergeS(mid+1, right)
            return merge(l1, l2)
        if not lists:
            return None
        return mergeS(0, len(lists)-1)
