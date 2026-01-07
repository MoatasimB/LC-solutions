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
                return
            
            # curr = node == p or node == q

            if p.val <= node.val <= q.val or q.val <= node.val <= p.val:
                ans = node
            
            elif p.val < node.val and q.val < node.val:
                dfs(node.left)
            else:
                dfs(node.right)
        
        dfs(root)
        return ans