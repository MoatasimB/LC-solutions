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
        
        prev = node
        curr = node.parent

        if curr and curr.left == prev:
            return curr
        
        while curr and curr.parent:
            prev = curr
            curr = curr.parent
            if curr.left == prev:
                return curr
        
        return None