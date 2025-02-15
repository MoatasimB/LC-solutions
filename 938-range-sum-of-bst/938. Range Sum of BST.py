# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        def dfs(root):
            if not root:
                return 0
            # if root.val < low or root.val > high:
            #     return 0
            ans = 0
            if low <= root.val <= high:
                ans += root.val
            
            ans += dfs(root.left) + dfs(root.right)

            return ans
        
        return dfs(root)
            
            