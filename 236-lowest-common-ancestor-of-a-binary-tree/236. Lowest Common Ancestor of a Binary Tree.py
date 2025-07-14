# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        ans = None

        def dfs(root):
            nonlocal ans
            if not root:
                return False

            left = dfs(root.left)
            right = dfs(root.right)

            if left and right:
                ans = root
                return False
            
            if (root == p or root == q) and (left or right):
                ans = root
                return False
            
            if root == p or root == q or left or right:
                return True
            
            return False
        
        dfs(root)
        return ans
            
