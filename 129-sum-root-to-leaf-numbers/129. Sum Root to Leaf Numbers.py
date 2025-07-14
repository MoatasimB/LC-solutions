# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        

        paths = []

        def dfs(root, curr):
            if not root:
                return
            

            new_curr = (curr * 10) + root.val

            if not root.left and not root.right:
                paths.append(new_curr)
            
            dfs(root.left, new_curr)
            dfs(root.right, new_curr)
        

        dfs(root, 0)
        return sum(paths)
            
            