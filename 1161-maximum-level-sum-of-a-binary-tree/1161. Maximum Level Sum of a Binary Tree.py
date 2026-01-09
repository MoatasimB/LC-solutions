# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        q = deque([root])
        ans = 0
        maxSum = float("-inf")
        level = 1
        while q:
            q_len = len(q)
            level_sum = 0
            for _ in range(q_len):

                node = q.popleft()
                level_sum += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            if level_sum > maxSum:
                maxSum = level_sum
                ans = level
            level += 1
        
        return ans