# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root, left, right):

            if not root:
                return True
            
            if root.val <= left or root.val >= right:
                return False
            
            l = dfs(root.left, left, min(root.val , right))
            r = dfs(root.right, max(root.val, left), right)

            return l and r
        
        return dfs(root, float('-inf'), float('inf'))