# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(root, curr):
            if not root:
                return False

            if curr == root.val and not root.left and not root.right:
                return True
            
            curr -= root.val

            if dfs(root.left, curr):
                return True
            if dfs(root.right, curr):
                return True
            
            return False
        
        return dfs(root, targetSum)