class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        def valid(r,c):
            return 0<=r<rows and 0<=c<cols
        
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        visited  = [[False] * cols for _ in range(rows)]
        def dfs(r,c):
            visited[r][c] = True

            for dx, dy in dirs:
                nr = dx + r
                nc = dy + c

                if valid(nr,nc) and not visited[nr][nc] and grid[nr][nc] == "1":
                    dfs(nr,nc)
        
        ans = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and not visited[r][c]:
                    dfs(r,c)
                    ans += 1
        
        return ans