# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if not root:
                return False
            
            elif check(root, subRoot):
                return True
            
            return dfs(root.left) or dfs(root.right)
        
        def check(r1, r2):

            if not r1 and not r2:
                return True
            if not r1 or not r2:
                return False
            
            return r1.val == r2.val and check(r1.left, r2.left) and check(r1.right, r2.right)
        
        return dfs(root)