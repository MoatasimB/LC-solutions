# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        
        levels = []
        i = 0
        n = len(traversal)

        while i < n:

            depth = 0
            while i < n and traversal[i] == "-":
                depth += 1
                i += 1
            
            val = 0
            while i < n and traversal[i].isdigit():
                val = (val * 10) + int(traversal[i])
                i += 1
            
            node = TreeNode(val)
            if depth >= len(levels):
                levels.append(node)
            else:
                levels[depth] = node
            
            if depth > 0:
                parent = levels[depth - 1]
                if not parent.left:
                    parent.left = node
                else:
                    parent.right = node
            
        return levels[0]
