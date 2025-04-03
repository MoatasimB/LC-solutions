# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        

        curr = root
        max_mode = 0
        curr_node = None
        mode = 0
        ans = []

        while curr:
            if curr.left:
                friend = curr.left
                while friend.right:
                    friend = friend.right
                
                friend.right = curr
                leftNode = curr.left
                curr.left = None
                curr = leftNode
            else:
                print(curr.val)
                if curr.val == curr_node:
                    mode +=1
                else:
                    mode = 1
                    curr_node = curr.val
                
                if mode > max_mode:
                    max_mode = mode
                    ans = [curr.val]
                elif mode == max_mode:
                    ans.append(curr.val)
            
                curr = curr.right
        return ans
