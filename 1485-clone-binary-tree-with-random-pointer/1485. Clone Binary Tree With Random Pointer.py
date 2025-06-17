# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':

        seen = {None:None}

        def dfs(node):
            if not node:
                return
            
            if node in seen:
                return seen[node]

            new_node = NodeCopy(node.val)
            seen[node] = new_node

            new_node.left = dfs(node.left)
            new_node.right = dfs(node.right)
            new_node.random = dfs(node.random)

            return new_node
    
        return dfs(root)

        