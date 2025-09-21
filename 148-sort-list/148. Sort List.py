# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def getMid(head):
            dummy = ListNode(-1, head)
            slow = dummy
            fast = head

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            
            mid = slow.next
            slow.next = None
            return mid

        
        def mergeSort(head):
            if not head or not head.next:
                return head 
            
            mid = getMid(head)

            left = mergeSort(head)
            right = mergeSort(mid)

            return merge(left, right)
        
        def merge(left, right):
            dummy = ListNode(-1)
            curr = dummy
            while left and right:
                if left.val < right.val:
                    curr.next = left
                    left = left.next
                else:
                    curr.next = right
                    right = right.next
                curr = curr.next
            
            curr.next = left if left else right

            return dummy.next
        
        return mergeSort(head)
