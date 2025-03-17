"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if not head:
            n = Node(insertVal)
            n.next = n
            return n
        prev = head
        curr = head.next
        flag = False
        while True:

            if prev.val <= insertVal <= curr.val:
                flag = True
            elif prev.val > curr.val:
                if insertVal >= prev.val or insertVal <= curr.val:
                    flag = True
            
            if flag:
                n = Node(insertVal)
                prev.next = n
                n.next = curr
                return head
            
            prev, curr = curr, curr.next
            if prev == head:
                break
        

        n = Node(insertVal)
        nextNode = head.next
        head.next = n
        n.next = nextNode
        return head

