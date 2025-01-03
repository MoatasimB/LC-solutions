# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        inorder = []

        def dfs(root):
            if not root:
                return
            dfs(root.left)
            inorder.append(root.val)
            dfs(root.right)
        
        dfs(root)
        ans = float("inf")
        for i in range(len(inorder)-1):
            if abs(inorder[i] - inorder[i+1]) < ans:
                ans = abs(inorder[i] - inorder[i+1])
        return ans