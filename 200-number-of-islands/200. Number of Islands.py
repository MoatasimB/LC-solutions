class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        m = len(grid)
        n = len(grid[0])

        def valid(r, c):
            return 0<=r<m and 0<=c<n

        dirs = [(0,1), (1,0), (-1,0), (0,-1)]
        
        def dfs(r, c):
            
            grid[r][c] = '0'
        
            for dx, dy in dirs:
                nr = dx + r
                nc = dy + c
                if valid(nr, nc) and grid[nr][nc] == "1":
                    dfs(nr,nc)
        
        ans = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1':
                    ans += 1
                    dfs(r,c)
        
        return ans
        