# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        counts = defaultdict(int)

        def dfs(node):
            if not node:
                return
            
            counts[node.val] += 1
            dfs(node.left)
            dfs(node.right)
        

        dfs(root)
        ans = []
        mode = 0
        for key, val in counts.items():
            if val > mode:
                mode = val
                ans = [key]
            elif val == mode:
                ans.append(key)
        
        return ans