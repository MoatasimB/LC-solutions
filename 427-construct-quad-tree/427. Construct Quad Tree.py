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


        def dfs(sR, sC, eR, eC):
            n = eR - sR + 1
            m = eC - sC + 1

            if n * m == 1:
                return Node(grid[sR][sC], True)
            curr_vals = set()
            only_val = None
            for r in range(sR, eR + 1):
                for c in range(sC, eC + 1):
                    if len(curr_vals) == 0:
                        curr_vals.add(grid[r][c])
                        only_val = grid[r][c]
                        continue
                    elif grid[r][c] not in curr_vals:

                        #make a new tree
                        top = sR
                        vertMid = (eR + sR) // 2

                        bottom = eR

                        left = sC
                        right = eC
                        horMid = (eC + sC) // 2

                        print(f"From Row: {sR} to Row: {eR}\nFrom Col: {sC} to Col: {eC}")
                        print("topleft",sR, sC, eR // 2, eC // 2)
                        print("topright", sR, (sC + eC // 2) + 1, eR // 2, eC)
                        print("bottomleft", (sR + eR // 2) + 1, sC, eR, eC // 2)
                        print("bottomright", (sR + eR // 2) + 1, (sC + eC // 2) + 1, eR, eC)
                        topleft = dfs(top, left, vertMid, horMid)
                        topright = dfs(top, horMid + 1, vertMid, right)
                        bottomleft =dfs(vertMid + 1, left, bottom, horMid)
                        bottomright = dfs(vertMid + 1, horMid + 1, bottom, right)
                        return Node(1, False, topleft, topright, bottomleft, bottomright)
            
            return Node(only_val, True)
        

        return dfs(0,0, len(grid) - 1, len(grid[0]) - 1)


        