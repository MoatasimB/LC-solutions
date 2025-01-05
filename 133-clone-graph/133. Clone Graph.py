"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        mpp = {} #original:copy
        if not node:
            return node
        def dfs(node):
            
            copy = Node(node.val)
            mpp[node] = copy
            for nei in node.neighbors:
                if nei not in mpp:   
                    copy.neighbors.append(dfs(nei))
                else:
                    copy.neighbors.append(mpp[nei])
            
            return copy
        
        return dfs(node)
