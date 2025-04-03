# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        

        curr_num = None
        mode = 0
        max_mode = 0
        ans = []
        def dfs(node):
            nonlocal curr_num
            nonlocal max_mode
            nonlocal mode
            nonlocal ans
        
            if not node:
                return
            
            dfs(node.left)
            
            if node.val == curr_num:
                mode += 1
            else:
                mode = 1
                curr_num = node.val
            
            if mode > max_mode:
                ans = [node.val]
                max_mode = mode
            elif mode == max_mode:
                ans.append(node.val)

            dfs(node.right)
        
        dfs(root)
        return ans