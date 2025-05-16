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
            if not node:
                return 0
            if not node.left and not node.right:
                return -1 
            

            left = dfs(node.left)
            right = dfs(node.right)

            if left == -1 or right == -1:
                ans += 1
                return 1
            
            elif left == 1 or right == 1:
                return 0
            
            elif left == 0 and right == 0:
                return -1
        
        final = dfs(root)

        if final == -1:
            ans += 1
        
        return ans

        
