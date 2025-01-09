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
        
        def make(top, bottom, left, right):
            
            # if top >= bottom or left >= right:
            #     return 
            vertMid = (top + bottom) // 2
            horMid = (left + right) // 2
            
            node = Node(None, None, None, None, None, None)
            
            if check(top, bottom, left , right):
                node.isLeaf = True
                node.val = grid[top][left]
            else:
                node.val = 0
                node.isLeaf = False
                node.topLeft = make(top, vertMid, left, horMid)
                node.topRight = make(top, vertMid, horMid, right)
                node.bottomLeft = make(vertMid, bottom, left, horMid)
                node.bottomRight = make(vertMid, bottom, horMid, right)
            return node


        
        
        
        def check(top, bottom, left, right):
            val = grid[top][left]
            print(val)

            for i in range(top, bottom):
                for j in range(left, right):
                    if grid[i][j] != val:
                        print("false")
                        return False
            print("true")
            return True
        r = len(grid)
        c = len(grid[0])
        return make(0,r, 0, c)
