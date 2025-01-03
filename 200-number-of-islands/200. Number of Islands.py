class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        
        def valid(r,c):
            return 0<=r<m and 0<=c<n

        dirs = [(0,1), (1,0), (0,-1), (-1,0)]

        def dfs(r,c):

            for dx, dy in dirs:
                new_r = r + dx
                new_c = c + dy

                if valid(new_r,new_c) and grid[new_r][new_c] == "1":
                    grid[new_r][new_c] = "0"
                    dfs(new_r,new_c)
        
        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    grid[i][j] == "0"
                    count +=1
                    dfs(i,j)
        return count
