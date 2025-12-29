# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        #prevHead
        #head
        #nextHead

        #prevHead -> prev (head of linked list after rev)
        #head -> nextHead

        #start again from head = nextHead

        dummy = ListNode(head)

        newStart = None

        prevHead = dummy
        start = head

        def rev(start):

            prev = None

            for _ in range(k):
                nextNode = start.next
                start.next = prev
                prev = start
                start = nextNode
            return prev


        while start:

            end = start

            for _ in range(k - 1):
                if not end:
                    break
                end = end.next
            
            if not end:
                return newStart if newStart else head
            nextNode = end.next

            # rev from start to end
            revHead = rev(start)
            if not newStart:
                newStart = revHead
            
            start.next = nextNode
            prevHead.next = revHead

            prevHead = start
            start = nextNode
        

        return newStart