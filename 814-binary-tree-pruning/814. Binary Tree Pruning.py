# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(node):
            if not node:
                return None
     
            left = dfs(node.left)
            right = dfs(node.right)

            node.left = left
            node.right = right

            if node.val  == 1:
                return node
            elif not left and not right:
                return None
            else:
                return node
    
        return dfs(root)