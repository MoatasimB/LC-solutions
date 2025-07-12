# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists:
            return None
        def merge(l1, l2):

            dummy = ListNode(-1)
            curr = dummy

            while l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                
                curr = curr.next
            
            if l1:
                curr.next = l1
            if l2:
                curr.next = l2
            
            return dummy.next
        

        def mergeSort(left, right):
            print(left, right)
            if left >= right:
                return lists[left]
            
            mid = (left + right) // 2

            l = mergeSort(left, mid)
            r = mergeSort(mid + 1, right)

            return merge(l,r)
        

        return mergeSort(0, len(lists) - 1)
