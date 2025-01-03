# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque([root])

        ans = []

        while q:
            size = len(q)
            curr = []
            for i in range(size):
                node = q.popleft()

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
                curr.append(node.val)
            ans.append(curr)
        
        for i in range(len(ans)):
            if i % 2:
                ans[i].reverse()
        
        return ans