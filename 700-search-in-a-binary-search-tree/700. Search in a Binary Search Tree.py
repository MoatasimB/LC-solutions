# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        ans = None
        def dfs(node):
            nonlocal ans
            if not node:
                return False
            
            if node.val == val:
                ans = node
                return True
            
            if val < node.val:
                if dfs(node.left):
                    return True
            else:
                if dfs(node.right):
                    return True
        dfs(root)
        return ans