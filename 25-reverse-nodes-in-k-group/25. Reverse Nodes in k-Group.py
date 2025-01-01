# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        count = 0

        x = head
        while x:
            count +=1
            x = x.next
        
        def rev(n):
            prev = None
            for _ in range(k):
                # print(n.val)
                nextNode = n.next
                n.next = prev
                prev = n
                n = nextNode
            connection = None
            if n:
                connection = n
            # print(prev.val, connection.val)
            return [prev, connection]
        
        curr = head
        dummy = None
        p = None
        while count >= k:

            beg = curr
            startNode, connectingNode = rev(curr)
            if not dummy:
                dummy = startNode

            beg.next = connectingNode
            if p:
                p.next = startNode

            p = beg
            curr = connectingNode
            count -= k
        

        return dummy


