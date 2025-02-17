class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        
        islands = {}

        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        
        def valid(r,c):
            return 0<=r<len(grid) and 0<=c<len(grid[0])

        group = 2

        def dfs(r, c, group):
            ans = 1
            grid[r][c] = group
            for dx, dy in dirs:
                nr, nc = r + dx, c + dy

                if valid(nr, nc) and grid[nr][nc] == 1:
                    ans += dfs(nr,nc,group)
            
            return ans
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    x = dfs(i,j, group)
                    islands[group] = x
                    group += 1
        final = 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    curr = 1
                    nei = set()
                    for dx, dy in dirs:
                        nr,nc = i+ dx, j + dy
                        if valid(nr, nc) and grid[nr][nc] in islands and grid[nr][nc] not in nei:
                            nei.add(grid[nr][nc])
                            curr += islands[grid[nr][nc]]
                    
                    final = max(curr, final)
        maxNoChange = 0
        if islands:
            maxNoChange = max(islands.values())

        return max(final, maxNoChange)



