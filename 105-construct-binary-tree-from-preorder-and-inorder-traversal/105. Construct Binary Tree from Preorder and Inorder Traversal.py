# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {val : i for i, val in enumerate(inorder)}
        
        
        i = 0
        def dfs(left, right):
            nonlocal i
            if left > right:
                return None
            
            
            node = TreeNode(preorder[i])
            
            i += 1
            node.left = dfs(left, indices[node.val] - 1)
            
            
            node.right = dfs(indices[node.val] + 1, right)
            
            return node
        
        
        return dfs(0, len(inorder) - 1)
            
        
        
        
            
            