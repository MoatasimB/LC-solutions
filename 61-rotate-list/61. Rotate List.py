# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head or k == 0:
            return head
        
        dummy = ListNode(0, head)
        slow = dummy
        fast  = head
        
        x = head
        count = 0
        while x:
            count +=1
            x = x.next
        k = k % count

        if k == 0:
            return head
        

        for _ in range(k):
            fast = fast.next
        
        while fast:
            fast = fast.next
            slow = slow.next
        
        newHead = slow.next

        slow.next = None


        curr = newHead

        if not curr:
            return slow

        while curr.next:
            curr = curr.next
        
        curr.next = head

        return newHead