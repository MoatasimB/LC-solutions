# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':

        nodes = set(nodes)
        ans = None
        def dfs(node):
            nonlocal ans
            if not node:
                return 0
            
            count = 0
            left = dfs(node.left)
            right = dfs(node.right)

            if node in nodes:
                count += 1
            
            count += left + right

            if count == len(nodes) and not ans:
                ans = node
            
            return count
        
        dfs(root)
        return ans