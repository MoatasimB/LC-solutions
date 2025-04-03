"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Optional[Node]':
        
        if node.right:
            curr = node.right
            while curr.left:
                curr = curr.left
            return curr
        # if node.parent.right == node:
        #     return None
        
        curr = node
        while curr.parent:
            curr = curr.parent
            if curr.val > node.val:
                return curr
        
        return None