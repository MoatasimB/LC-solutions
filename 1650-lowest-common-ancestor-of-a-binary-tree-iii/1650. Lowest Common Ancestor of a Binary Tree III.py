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
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        
        ancestors = set()

        h1 = p
        while h1:
            ancestors.add(h1)
            h1 = h1.parent
        

        h2 = q
        while h2:
            if h2 in ancestors:
                return h2
            h2 = h2.parent
            