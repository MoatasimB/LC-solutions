# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = float('-inf')
        def dfs(root):
            nonlocal ans
            
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)

            ans = max(ans, root.val + left + right)
            next = max(0,left,right)
            if next == 0:
                return max(0,root.val)
            else:
                return max(0,next + root.val)
        
        dfs(root)
        return ans