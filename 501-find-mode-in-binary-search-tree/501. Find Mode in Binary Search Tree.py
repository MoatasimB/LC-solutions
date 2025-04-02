# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        ans = []
        mode = 0
        curr_num = 0
        max_mode = 0

        curr = root

        while curr:
            if curr.left:

                friend = curr.left
                while friend.right:
                    friend = friend.right
                
                friend.right = curr

                left_node = curr.left
                curr.left = None
                curr = left_node
            
            else:
                if curr.val == curr_num:
                    mode +=1
                else:
                    mode = 1
                    curr_num = curr.val
                
                if mode > max_mode:
                    ans = [curr_num]
                    max_mode = mode
                elif mode == max_mode:
                    ans.append(curr_num)
                
                curr = curr.right
        
        return ans