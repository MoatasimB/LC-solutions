class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        m = len(grid)
        n = len(grid[0])

        def valid(r, c):
            return 0<=r<m and 0<=c<n

        dirs = [(0,1), (1,0), (-1,0), (0,-1)]
        
        def dfs(r, c):
            
            if (r,c) in seen:
                return
            
            seen.add((r,c))

            for dx, dy in dirs:
                nr = dx + r
                nc = dy + c
                if valid(nr, nc) and (nr, nc) not in seen and grid[nr][nc] == "1":
                    dfs(nr,nc)
        
        seen = set()
        ans = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1' and (r,c) not in seen:
                    ans += 1
                    dfs(r,c)
        
        return ans
        