# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        def merge(head1: Optional[ListNode], head2: Optional[ListNode]) -> Optional[ListNode]:

            dummy = ListNode(-1)
            curr = dummy

            while head1 and head2:
                if head1.val < head2.val:
                    curr.next = head1
                    head1 = head1.next
                else:
                    curr.next = head2
                    head2 = head2.next
                curr = curr.next
            
            if head1:
                curr.next = head1
            if head2:
                curr.next = head2
            return dummy.next

        def mergesort(l: int, r: int) -> Optional[ListNode]:
            if l == r:
                return lists[l]
            mid = (l + r) // 2
            left = mergesort(l, mid)
            right = mergesort(mid + 1, r)
            
            return merge(left, right)
        
        return mergesort(0, len(lists) - 1)