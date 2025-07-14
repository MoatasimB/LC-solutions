# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []
        q = deque([root])
        ans = []
        while q:
            q_len = len(q)
            
            max_node = float('-inf')
            for _ in range(q_len):
                node = q.popleft()

                max_node = max(max_node, node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            ans.append(max_node)
        
        return ans