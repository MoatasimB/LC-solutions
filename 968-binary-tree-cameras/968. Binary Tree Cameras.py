# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        
        ans = 0
        def dfs(node):
            nonlocal ans
            l = 0
            r = 0
            if not node.left and not node.right:
                return -1
            
            if node.left:
                l = dfs(node.left)
            if node.right:
                r = dfs(node.right)

            if l == -1 or r == -1:
                ans += 1
                return 1

            if l == 1 or r == 1:
                return 0
            
            if l == 0 and r == 0:
                return -1
            
        
        final = dfs(root)
        if final == -1:
            ans += 1

        return ans
