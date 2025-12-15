"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)

        def dfs(l, r, t, b):
            isLeaf = True
            node = Node(val = 0, topLeft = None, topRight = None, bottomLeft=None, bottomRight=None)
            vals = set()
            for i in range(t, b + 1):
                for j in range(l, r + 1):
                    vals.add(grid[i][j])
                    if len(vals) > 1:
                        isLeaf = False
                        break
                if not isLeaf:
                    break
            if isLeaf:
                nodeVal = None
                for val in vals:
                    nodeVal = val
                node.val = nodeVal
                node.isLeaf = True
            else:
                midRow = (t + b) // 2
                midCol = (l + r) // 2
                node.topLeft = dfs(l, midCol, t, midRow)
                node.topRight = dfs(midCol + 1, r, t, midRow)
                node.bottomLeft = dfs(l, midCol, midRow + 1, b)
                node.bottomRight = dfs(midCol + 1, r, midRow + 1, b)
                node.isLeaf = False

            return node
        
        return dfs(0, n - 1, 0, n - 1)



