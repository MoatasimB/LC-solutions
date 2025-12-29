# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        
        heightAfterRemoval = {}
        maxH = 0
        def dfsLtoR(root, depth):
            nonlocal maxH
            if not root:
                return
            
            heightAfterRemoval[root.val] = maxH
            maxH = max(maxH, depth)

            dfsLtoR(root.left, depth + 1)
            dfsLtoR(root.right, depth + 1)
        
        dfsLtoR(root, 0)

        maxH = 0
        def dfsRtoL(root, depth):
            nonlocal maxH
            if not root:
                return
            
            heightAfterRemoval[root.val] = max(heightAfterRemoval[root.val], maxH)
            maxH = max(maxH, depth)

            dfsRtoL(root.right, depth + 1)
            dfsRtoL(root.left, depth + 1)
        
        
        dfsRtoL(root, 0)

        
        return [heightAfterRemoval[q] for q in queries]