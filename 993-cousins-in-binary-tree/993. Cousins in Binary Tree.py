# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        

        q = deque()
        q.append([root, -1])

        found_x = False
        par_x = None
        found_y = False
        par_y = None
        while q:
            q_length = len(q)
            for _ in range(q_length):
                node, parent = q.popleft()


                if node.val == x:
                    found_x = True
                    par_x = parent
                
                if node.val == y:
                    found_y = True
                    par_y = parent
                
                if node.left:
                    q.append([node.left, node])
                
                if node.right:
                    q.append([node.right, node])
            if found_x and found_y and (par_y != par_x):
                    return True
                
            if found_x or found_y:
                    return False
        
        return False
