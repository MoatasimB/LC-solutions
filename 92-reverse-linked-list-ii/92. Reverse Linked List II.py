# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # if right - left == 0:
        #     return head
        dummy = ListNode(-1)
        dummy.next = head
        x = dummy

        slow = head
        fast = head

        for _ in range(right - left):
            fast = fast.next
        
        for _ in range(left-1):
            dummy = dummy.next
            slow = slow.next
            fast = fast.next
        
        finalNode = fast.next
        startNode = slow
        prev = None
        for _ in range(right - left + 1):
            nextNode = slow.next
            slow.next = prev
            prev = slow
            slow = nextNode
        
        dummy.next = prev
        startNode.next = finalNode

        return x.next


        

