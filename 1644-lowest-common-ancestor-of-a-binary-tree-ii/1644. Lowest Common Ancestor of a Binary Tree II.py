# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        ans = None

        def dfs(node):
            nonlocal ans
            if not node:
                return False
            
            left = dfs(node.left)
            right = dfs(node.right)

            curr = (node == p or node == q)

            if left and right:
                ans = node
            if curr and (left or right):
                ans = node
            return curr or left or right
        
        dfs(root)
        return ans