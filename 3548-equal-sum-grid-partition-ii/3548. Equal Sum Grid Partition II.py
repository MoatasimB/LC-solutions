class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:

        total = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                total += grid[r][c]
       
        def rotate(grid):
            m = len(grid)
            n = len(grid[0])
            new = [[0] * m for _ in range(n)]
            for r in range(m):
                for c in range(n):
                    new[c][m - r - 1] = grid[r][c]
            return new


        for _ in range(4):
            seen = set()
            seen.add(0)
            m = len(grid)
            n = len(grid[0])
            curr = 0
            if m == 1:
                grid = rotate(grid)
                continue
            if n == 1:
                for i in range(m - 1):
                    curr += grid[i][0]
                    need = (2 * curr) - total

                    if need == 0 or need == grid[0][0] or need == grid[i][0]:
                        return True
                grid = rotate(grid)
                continue
            
            for r in range(m - 1):
                for c in range(n):
                    seen.add(grid[r][c])
                    curr += grid[r][c]
                
                need = (2 * curr) - total
                if r == 0:
                    if grid[0][0] == need or need == 0 or grid[0][n - 1] == need:
                        return True
                else:
                    if need in seen:
                        return True
            grid = rotate(grid)
        return False
                    
                    


