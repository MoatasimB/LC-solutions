class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        def valid(r, c):
            return 0 <= r < row and 0 <= c < col
        
        dirs = [(0, 1), (1,0), (0,-1), (-1,0)]

        def check(day):
            grid = [[0] * col for _ in range(row)]

            for i in range(day + 1):
                wr, wc = cells[i]
                grid[wr - 1][wc - 1] = 1
            
            for c in range(col):
                if grid[0][c] == 0 and dfs(0, c, grid):
                    return True
            
            return False
        
        def dfs(r, c, grid):
            if r == row - 1:
                return True
            
            for dx, dy in dirs:
                nr = r + dx
                nc = c + dy
                if valid(nr, nc) and grid[nr][nc] == 0:
                    grid[nr][nc] = 1
                    if dfs(nr, nc, grid):
                        return True
            
            return False
        
        l = 0
        r = len(cells) - 1


        while l <= r:
            mid = (l + r) // 2

            if check(mid):
                l = mid + 1
            else:
                r = mid - 1
        
        return r + 1