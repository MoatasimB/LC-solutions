class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        def bfs(i,j):
            nonlocal ans
            q = deque()
            q.append((i,j, 0)) #r,c, dist
            while q:
                r,c,dist  = q.popleft()

                for dx, dy in dirs:
                    nr, nc = dx + r, dy + c

                    if valid(nr, nc):
                        grid[nr][nc] -= 1
                        dist_dic[(nr, nc)] += dist + 1
                        ans = min(ans, dist_dic[(nr, nc)])
                        q.append((nr,nc,dist+1))
            
        def valid(r,c):
            return 0<=r<n and 0<=c<m and grid[r][c] == curr_land_exploration
        
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
    
        dist_dic = {}
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    dist_dic[(i,j)] = 0
        curr_land_exploration = 0
        #multisource BFS
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    ans = float('inf')
                    bfs(i,j)
                    curr_land_exploration -= 1
                    
    
        return ans if ans != float('inf') else -1
        