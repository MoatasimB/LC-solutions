# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return
        
        q = deque()
        
        q.append(root)
        
        ans = []
        curr = 0
        while q:
            
            n = len(q)
            
            curr_level = []
            
            for _ in range(n):
                node = q.popleft()
                
                curr_level.append(node.val)
                

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
            if curr % 2==0:
                ans.append(curr_level)
            else:
                x = []
                for i in range(len(curr_level) -1, -1, -1):
                    x.append(curr_level[i])

                ans.append(x)
                
            curr +=1
                        
        
        return ans
        