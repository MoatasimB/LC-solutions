# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        ans = 0
        def dfs(root):
            nonlocal ans
            if not root:
                return [0, 0]
            
            leftSum, leftCount = dfs(root.left)
            rightSum, rightCount = dfs(root.right)
            totalCount = leftCount + rightCount + 1
            totalSum = leftSum + rightSum + root.val
            if totalSum // totalCount == root.val:
                ans += 1
            return [totalSum, totalCount]
        
        dfs(root)
        return ans