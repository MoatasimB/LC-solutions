# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        
        hAfterRem = {}
        maxH = 0
        def dfsLR(node, depth):
            nonlocal maxH
            if not node:
                return
            
            hAfterRem[node.val] = maxH
            maxH = max(maxH, depth)

            dfsLR(node.left, depth + 1)
            dfsLR(node.right, depth + 1)
        
        dfsLR(root, 0)
        maxH = 0
        def dfsRL(node, depth):
            nonlocal maxH
            if not node:
                return
            
            hAfterRem[node.val] = max(maxH, hAfterRem[node.val])
            maxH = max(maxH, depth)

            dfsRL(node.right, depth + 1)
            dfsRL(node.left, depth + 1)
        
        dfsRL(root, 0)

        return [hAfterRem[q] for q in queries]