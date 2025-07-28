class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        

        islands = {} #id:size
        m = len(grid)
        n = len(grid[0])

        dirs = [(0,1), (0,-1), (1,0), (-1,0)]

        def valid(r,c):
            return 0<=r<m and 0<=c<n

        def dfs(r,c, id):
            size = 1
            for dx, dy in dirs:
                nr = r + dx
                nc = c + dy
                if valid(nr, nc) and grid[nr][nc] == 1:
                    grid[nr][nc] = id
                    size += dfs(nr,nc,id)
    
            return size
        
        current_id = -1
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    grid[r][c] = current_id
                    s = dfs(r,c, current_id)
                    islands[current_id] = s
                    current_id -= 1

        ans = max(islands.values()) if len(islands) > 0 else 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    curr = 1
                    nei = set() #contains id's that this island is apart of
                    for dx, dy in dirs:
                        nr, nc = r + dx, c + dy

                        if valid(nr,nc) and grid[nr][nc] in islands and grid[nr][nc] not in nei :
                            curr += islands[grid[nr][nc]]
                            nei.add(grid[nr][nc])
                    
                    ans = max(ans, curr)

        return ans



