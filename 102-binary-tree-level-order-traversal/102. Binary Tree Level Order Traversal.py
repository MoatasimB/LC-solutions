# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque([root])
        ans = []
        while q:
            # print(q)
            # print("____________")
            
            curr = []
            for _ in range(len(q)):
                node = q.popleft()
                # if not node:
                #     print(q)
                # if node:
                curr.append(node.val)

                if node and node.left:
                    q.append(node.left)
                if node and node.right:
                    q.append(node.right)
                
            ans.append(curr)
        return ans

        