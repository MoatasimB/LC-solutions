# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        inorder = []
        def dfs(root):
            if not root:
                return
            
            left = dfs(root.left)
            inorder.append(root.val)
            right = dfs(root.right)
        dfs(root)
        for i in range(len(inorder)-1):
            if (inorder[i] >= inorder[i+1]):
                return False
        
        return True