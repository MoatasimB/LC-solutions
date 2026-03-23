class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        

        def rotate(grid):
            m = len(grid)
            n = len(grid[0])

            for r in range(m):
                for c in range(r):
                    grid[r][c], grid[c][r] = grid[c][r], grid[r][c]
            
            for row in grid:
                l = 0
                r = n - 1

                while l < r:
                    row[l], row[r] = row[r], row[l]
                    l += 1
                    r -= 1
        if mat == target:
            return True
        for _ in range(4):
            rotate(mat)
            if mat == target:
                return True
        
        return False