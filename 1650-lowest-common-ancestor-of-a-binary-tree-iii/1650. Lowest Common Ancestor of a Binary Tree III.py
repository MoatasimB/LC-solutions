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
        
        def depth(node):
            d = 0
            n = node
            while n.parent:
                n = n.parent
                d += 1
            return d
        
        pDepth = depth(p)
        qDepth = depth(q)
        print(pDepth, qDepth)

        while pDepth < qDepth:
            q = q.parent
            qDepth -= 1
        
        while qDepth < pDepth:
            p = p.parent
            pDepth -= 1
        
        while q!=p:
            q = q.parent
            p = p.parent
        
        return p
