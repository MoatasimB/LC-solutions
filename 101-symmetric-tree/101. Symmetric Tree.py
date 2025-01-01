# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(rootX, rootY):

            if not rootX and not rootY:
                return True
            
            if (not rootX and rootY) or (rootX and not rootY):
                return False
            
            if rootX.val != rootY.val:
                return False

            left = dfs(rootX.left, rootY.right)
            right = dfs(rootX.right, rootY.left)

            return left and right
        
        return dfs(root.left, root.right)
