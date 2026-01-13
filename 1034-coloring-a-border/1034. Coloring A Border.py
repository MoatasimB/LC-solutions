class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        
        [1,3,3],
        [2,3,3]

        [1,1,1],
        [1,1,1],
        [1,1,1]

        m = len(grid)
        n = len(grid[0])

        def valid(r, c):
            return 0 <= r < m and 0 <= c < n
        
        dirs = [(0, 1), (1,0), (0,-1), (-1,0)]

        q = deque([[row, col, grid[row][col]]])
        seen = set([(row, col)])

        cellsToColor = set()
        while q:
            r, c, origColor = q.popleft()

            sides = 0

            for dx, dy in dirs:
                nr = r + dx
                nc = c + dy
                if valid(nr, nc) and grid[nr][nc] == origColor:
                    sides += 1
                    if (nr, nc) not in seen:
                        seen.add((nr, nc))
                        q.append([nr, nc, origColor])
            
            if sides != 4:
                cellsToColor.add((r, c))
        

        for r, c in cellsToColor:
            grid[r][c] = color
        
        return grid
                    