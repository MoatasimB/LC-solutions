# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        smaller = ListNode(0)
        larger = ListNode(0)

        X = smaller
        y = larger

        curr = head

        while curr:
            nextNode = curr.next
            
            if curr.val < x:
                X.next = curr
                X = curr
            else:
                y.next = curr
                y = curr

            curr.next = None
            curr = nextNode


        X.next = larger.next

        return smaller.next
