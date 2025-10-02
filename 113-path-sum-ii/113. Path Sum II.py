# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        ans = []
        def dfs(node, target, curr):
            if not node:
                return

            
            left = dfs(node.left, target - node.val, curr + [node.val])
            right = dfs(node.right, target - node.val, curr + [node.val])
            
            if not node.left and not node.right:
                if target - node.val == 0:
                    curr.append(node.val)
                    ans.append(curr[:])
                    curr.pop()


        dfs(root, targetSum, [])
        return ans            
 
