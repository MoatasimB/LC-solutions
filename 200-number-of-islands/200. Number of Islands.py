class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        seen = [[False] * COLS for _ in range(ROWS)]
        def valid(r,c):
            return 0<=r<ROWS and 0<=c<COLS
        
        def dfs(r,c):
            for dx, dy in dirs:
                new_r = r + dx
                new_c = c + dy

                if valid(new_r, new_c) and grid[new_r][new_c] == "1" and not seen[new_r][new_c]:
                    seen[new_r][new_c] = True
                    dfs(new_r, new_c)
        

        ans = 0

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1" and not seen[i][j]:
                    ans +=1
                    seen[i][j] = True
                    dfs(i,j)
        
        return ans
            


            