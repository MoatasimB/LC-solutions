# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        sumOfSubtree = defaultdict(int)

        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            sumOfSubtree[node] = node.val + left + right

            return node.val + left + right
        dfs(root)
        final = 0
        def findMax(node):
            nonlocal final

            if not node:
                return

            findMax(node.left)
            findMax(node.right)
            total = sumOfSubtree[root]
            left = node.left if node.left else None
            right = node.right if node.right else None

            if left:
                left_sum = sumOfSubtree[left]
                final = max(final, left_sum * (total - left_sum))

            
            if right:
                right_sum = sumOfSubtree[right]
                final = max(final, right_sum * (total - right_sum))
        

        findMax(root)
       
        return final % (10**9 + 7)
            

            
