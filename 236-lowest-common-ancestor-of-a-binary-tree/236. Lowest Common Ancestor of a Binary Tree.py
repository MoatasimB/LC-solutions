# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = root
        def dfs(root):
            nonlocal ans

            if not root:
                return False
            
    
            left = dfs(root.left)
            right = dfs(root.right)

            curr = False

            if root == p or root == q:
                curr = True
            
            if (curr and left) or (curr and right) or (left and right):
                ans = root
            
            
            return curr or left or right
        
        dfs(root)
        return ans