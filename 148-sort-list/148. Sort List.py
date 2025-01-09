# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        

        def getMid(head):

            slow = ListNode(-1, head)
            fast = head

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            
            mid = slow.next
            slow.next = None
            return mid
        
        def mergeS(head):
            if not head or not head.next:
                return head
            
            mid = getMid(head)

            l = mergeS(head)
            r = mergeS(mid)
            return merge(l,r)
        
        def merge(l,r):
            dummy = ListNode(-1)
            curr = dummy

            while l and r:
                if l.val < r.val:
                    curr.next = l
                    l = l.next
                else:
                    curr.next = r
                    r = r.next
                curr = curr.next
            
            curr.next = l if l else r

            return dummy.next
        
        return mergeS(head)