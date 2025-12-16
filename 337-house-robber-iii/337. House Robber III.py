# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        memo = {}
        def dfs(node, prevRobbed):
            if (node, prevRobbed) in memo:
                return memo[(node, prevRobbed)]
            if not node:
                return 0
            
            if prevRobbed:
                memo[(node, prevRobbed)] = dfs(node.left, False) + dfs(node.right, False)
                return memo[(node, prevRobbed)]
            #take this node and dont take this node
            take = node.val + dfs(node.left, True) + dfs(node.right, True)
            skip = dfs(node.left, False) + dfs(node.right, False)
            memo[(node, prevRobbed)] = max(take, skip)
            return memo[(node, prevRobbed)]
        
        return dfs(root, False)