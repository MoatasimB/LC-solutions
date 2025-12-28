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
        front = True
        while q:
            q_len = len(q)
            curr = deque()
            for _ in range(q_len):
                node = q.popleft()

                if front:
                    curr.append(node.val)
                else:
                    curr.appendleft(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(list(curr))
            front = not front


        # for i in range(1, len(ans), 2):
            
        #     l = 0
        #     r = len(ans[i]) - 1

        #     while l < r:

        #         ans[i][l], ans[i][r] = ans[i][r], ans[i][l]
        #         l += 1
        #         r -= 1
        
        return ans
        