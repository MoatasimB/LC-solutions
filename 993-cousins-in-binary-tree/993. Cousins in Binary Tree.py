# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        
        depth_x = 0
        depth_y = 0
        par_x = None
        par_y = None

        def dfs(root, depth, parent):
            nonlocal depth_x, depth_y, par_x, par_y
            if not root:
                return
            
            if root.val == x:
                depth_x = depth
                par_x = parent
            if root.val == y:
                depth_y = depth
                par_y = parent

            left = dfs(root.left, depth + 1, root)
            right = dfs(root.right, depth + 1, root)

        dfs(root, 0, -1)

        return depth_x == depth_y and par_x != par_y