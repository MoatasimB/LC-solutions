# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        q = deque()

        q.append(root)

        ans = []

        while q:
            size = len(q)
            sum = 0
            for _ in range(size):
                node = q.popleft()

                sum += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            ans.append(sum/size)
        
        return ans
