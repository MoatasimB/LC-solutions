# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        #max(dfs(node, True), dfs(node. False))
        memo = {}
        def dfs(node, parentRobbed):
            if (node, parentRobbed) in memo:
                return memo[(node, parentRobbed)]
            if not node:
                return 0
            

            if parentRobbed:
                memo[(node, parentRobbed)] = dfs(node.left, False) + dfs(node.right, False)
                return memo[(node, parentRobbed)]
            else:
                memo[(node, parentRobbed)] = max(node.val + dfs(node.left, True) + dfs(node.right, True), dfs(node.left, False) + dfs(node.right, False))
                return memo[(node, parentRobbed)]
        
        return max(dfs(root, True), dfs(root, False))
        

            
