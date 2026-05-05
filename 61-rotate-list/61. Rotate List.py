# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head
        dummy = ListNode(-1, head)
        curr = head
        last = None
        n = 0
        while curr:
            n += 1
            if not curr.next:
                last = curr
            curr = curr.next
        
        count = 0
        curr = head
        k = k % n
        if k == 0:
            return head
        while curr:
            count += 1
            if count == n - k:
                break
            curr = curr.next
        nextNode = curr.next
        curr.next = None
        last.next = head

        return nextNode