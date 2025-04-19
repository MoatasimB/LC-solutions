class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        def valid(r,c):
            return 0<=r<n and 0<=c<m
        
        dirs = [[0,1], [0, -1], [1,0], [-1,0]]

        def dfs(r,c):

            seen.add((r,c))

            for dx, dy in dirs:
                nr, nc = r + dx, c + dy

                if valid(nr, nc) and (nr,nc) not in seen and grid[nr][nc] == 0:
                    dfs(nr,nc)
        

        seen = set()
        
        for c in range(m):
            if grid[0][c] == 0 and (0,c) not in seen:
                dfs(0,c)
            if grid[n - 1][c] == 0 and (n - 1,c) not in seen:
                dfs(n - 1,c)
        for r in range(n):
            if grid[r][0] == 0 and (r,0) not in seen:
                dfs(r,0)
            if grid[r][m - 1] == 0 and (r,m - 1) not in seen:
                dfs(r,m - 1)
        ans = 0
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 0 and (r,c) not in seen:
                    dfs(r,c)
                    ans += 1
        
        return ans

        [[X,1,1,1,1,1,1,1],
         [1,0,1,0,0,0,0,1],
         [1,0,0,0,0,1,0,1],
         [0,1,0,0,0,1,0,1],
         [1,0,0,1,0,1,0,1],
         [1,1,1,1,0,0,1,1],
         [1,0,0,0,0,0,1,1],
         [X,1,1,1,1,1,1,1]]