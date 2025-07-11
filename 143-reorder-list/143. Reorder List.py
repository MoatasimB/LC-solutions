# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head
        slow_pre = ListNode(-1, slow)


        while fast and fast.next:
            slow = slow.next
            slow_pre = slow_pre.next
            fast = fast.next.next
        if fast == slow:
            return head

        prev = None
        slow_pre.next = None
        while slow:
            nextNode = slow.next
            slow.next = prev
            prev = slow
            slow = nextNode
        

        dummy = ListNode(-1)
        curr = dummy


        while prev:
            nextP = prev.next

            nextH = None
            if head:
                nextH = head.next
                curr.next = head
                curr = curr.next

            curr.next = prev
            curr = curr.next


            prev = nextP
            head = nextH
        
        return dummy.next


