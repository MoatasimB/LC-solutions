# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        ans = 0
        def dfs(root, curr):
            nonlocal ans
            if not root:
                return
    
            curr = (curr * 10) + root.val

            dfs(root.left, curr)
            dfs(root.right, curr)

                    
            if not root.left and not root.right:
                ans += curr
        
        dfs(root, 0)
        return ans