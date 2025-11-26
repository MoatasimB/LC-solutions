"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        def dfs(root):
            if not root:
                return 0
            maxPath = 0
            for child in root.children:
                maxPath = max(maxPath, dfs(child))
            
            return maxPath + 1
        
        return dfs(root)
