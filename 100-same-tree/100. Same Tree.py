# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def dfs(rootX, rootY):

            if rootX and not rootY:
                return False
            if rootY and not rootX:
                return False
            
            if not rootX and not rootY:
                return True
            
            if rootX.val != rootY.val:
                return False

            left = dfs(rootX.left, rootY.left)
            right = dfs(rootX.right, rootY.right)

            return left and right
        
        return dfs(p,q)