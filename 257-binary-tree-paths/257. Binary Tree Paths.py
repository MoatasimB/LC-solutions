# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        ans = []

        def dfs(root, curr):
            if not root:
                return
            if not root.left and not root.right:
                curr += str(root.val)
                ans.append(curr)
                return
            
           
            dfs(root.left, curr + str(root.val) + "->")
            dfs(root.right, curr + str(root.val) + "->")
        
        dfs(root, "")
        return ans