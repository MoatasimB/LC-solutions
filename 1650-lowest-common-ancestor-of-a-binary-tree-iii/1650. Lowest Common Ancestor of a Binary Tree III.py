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
        
        def dfs(root):
            if not root:
                return [False, None]
     
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            if left[1] != None or right[1]!= None:
                return [True, left[1] if left[1] else right[1]]
            if left[0] and right[0] and left[1] == None:
                return [True, root]
            if (left[0] or right[0]) and (root == p or root == q):
                return [True, root]
       
            if root == p or root == q:
                return [True, None]
            if left[0] or right[0]:
                return [True, None]
            
            return [False, None]
        
        curr = p 
        while curr.parent != None:
            curr = curr.parent
        return dfs(curr)[1]
            
