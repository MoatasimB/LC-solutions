# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        
        ans = 0
        distance = 0
        def dfs(root):
            nonlocal ans
            nonlocal distance
            depth = 0

            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)

            if root.val == start:
                distance = max(left, right)
                ans = max(ans, distance )
                depth = -1
            elif left >=0 and right >=0:
                depth = max(left, right) + 1
            else:
                ans = max(ans, abs(left) + abs(right))
                depth = min(left, right) - 1

            return depth
        
        dfs(root)
        return ans
