# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        if not root: return None
        copies = {}
        def dfs(node):
            if not node:
                return None
            
            copy = NodeCopy(node.val)
            copy.left = dfs(node.left)
            copy.right = dfs(node.right)
            copies[node] = copy
            return copy



        dfs(root)
        for node, copy in copies.items():
            if node.random:
                copy.random = copies[node.random]
        return copies[root]