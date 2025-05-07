# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        
        i = 0
        def dfs():
            nonlocal i

            if i >= len(s) or s[i] == ")":
                return None

            if s[i] == "(":
                i += 1
            
            sign = 1
            if s[i] == "-":
                sign = -1
                i += 1
            curr = 0
            while i < len(s) and s[i].isdigit():
                curr = (curr * 10 ) + int(s[i])
                i += 1
            i -= 1
            node = TreeNode(curr * sign)
            i += 1
            node.left = dfs()
            node.right = dfs()
            i+= 1
            return node

        
        return dfs()


