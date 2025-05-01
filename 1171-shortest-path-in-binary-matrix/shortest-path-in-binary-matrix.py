class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        n = len(grid)
        m = len(grid[0])
        if grid[0][0] != 0 or grid[n - 1][m - 1] != 0:
            return -1
        
        dirs = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
        def valid(r,c):
            return 0<=r<n and 0<=c<m and grid[r][c] == 0
        
        q = deque()
        seen = set()
        q.append((0,0,1))
        seen.add((0,0))

        while q:
            r, c, dist = q.popleft()

            if (r,c) == (n - 1, m - 1):
                return dist
            
            for dx, dy in dirs:
                nr, nc = r + dx, c + dy

                if valid(nr,nc) and (nr,nc) not in seen:
                    q.append((nr,nc,dist + 1))
                    seen.add((nr,nc))
        
        return -1

