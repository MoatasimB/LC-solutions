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
                return [False, None]
            
            left, n1 = dfs(root.left)
            right, n2 = dfs(root.right)
            if n1:
                return [True, n1]
            if n2:
                return [True, n2]
            if left and right:
                return [True, root]
                ans = root
            elif (root == p or root == q) and (left or right):
                return [True, root]
                ans = root
            
            if root == p or root == q or left or right:
                return [True, None]
            
            return [False, None]
        
        return dfs(root)[1]
        return ans

