# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        

        depths = {}

        def dfs(root, depth):

            if not root:
                return 
            
            if depth in depths:
                val = depths[depth]
                depths[depth] = max(val, root.val)
            else:
                depths[depth] = root.val
            
            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)
        

        dfs(root, 0)

        return list(depths.values())