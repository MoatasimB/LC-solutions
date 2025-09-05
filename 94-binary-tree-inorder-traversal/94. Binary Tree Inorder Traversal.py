# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        
        ans = []
        
        stack = []
        curr = root
        while stack or curr:
            
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            ans.append(curr.val)
            curr = curr.right
        
        return ans
                
        
        def dfs(root):
            if not root:
                return
            
            dfs(root.left)
            ans.append(root.val)
            dfs(root.right)
        
        dfs(root)
        return ans
    