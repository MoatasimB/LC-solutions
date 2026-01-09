class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        
        
        m = row
        n = col

        def valid(row, col):
            return 0<=row<m and 0<=col<n and grid[row][col] == 0
        
        directions = [(-1,0), (0,-1), (0,1), (1,0)]

        def check(day, r, c, grid):

            if r == m - 1:
                return True
            
            for dx, dy in directions:
                next_row = r + dx
                next_col = c + dy

                if valid(next_row, next_col):
                    grid[next_row][next_col] = 1
                    if check(day, next_row, next_col, grid):
                        return True
            
            return False
        
        left = 1
        right = len(cells)

        while left <= right:
            mid = (left + right) // 2

            res = False
                        
            grid = [[0] * n for _ in range(m)]
            for i in range(mid):
                r,c = cells[i]
                grid[r-1][c-1] = 1
            


            for i in range(n):
                if grid[0][i] == 0:
                    grid[0][i] == 1
                    if check(mid, 0, i, grid):
                        res = True
                        break

            if res:
                left = mid + 1
            else:
                right = mid - 1

        return right
                