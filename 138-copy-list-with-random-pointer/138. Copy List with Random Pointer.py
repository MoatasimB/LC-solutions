"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        nodes = {}
        # nodes[None] = None

        dummy = head
        n = Node(-1,None)
        new = n

        while dummy:
            NewNode = Node(dummy.val)
            new.next = NewNode
            nodes[dummy] = NewNode
            
            new = new.next
            dummy = dummy.next
        
        dummy = head
        new = n.next

        while dummy:
            if dummy.random in nodes:
                new.random = nodes[dummy.random]

            dummy = dummy.next
            new = new.next
        
        return n.next