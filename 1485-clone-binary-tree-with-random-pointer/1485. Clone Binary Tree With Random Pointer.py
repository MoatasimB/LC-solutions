# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        

        copy = {None:None}

        def dfs(node):

            if not node:
                return None
            
            new_node = NodeCopy(node.val)
            new_node.left = dfs(node.left)
            new_node.right = dfs(node.right)

            copy[node] = new_node

            return new_node

        n = dfs(root)


        def dfs2(old_node):
            if not old_node:
                return

            new_node = copy[old_node]
            new_node.random = copy[old_node.random]

            dfs2(old_node.left)
            dfs2(old_node.right)
        
        dfs2(root)

        return n



        