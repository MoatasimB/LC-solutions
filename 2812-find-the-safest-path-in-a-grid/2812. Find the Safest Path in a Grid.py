class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        if grid[0][0] == 1 or grid[m-1][n-1] == 1:
            return 0

        def valid(r, c):
            return 0<=r<m and 0<=c<n
        
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]

        def getMat():
            q = deque()
            seen = set()

            mat = [[0] * n for _ in range(m)]

            for r in range(m):
                for c in range(n):
                    if grid[r][c] == 1:
                        q.append([r, c, r, c]) #row, col, ogRow, ogCol
                        mat[r][c] = float("inf")
            
            while q:
                r, c, ogRow, ogCol = q.popleft()


                for dx, dy in dirs:
                    nr = r + dx
                    nc = c + dy
                    if valid(nr, nc) and mat[nr][nc] == 0:
                        mat[nr][nc] = abs(nr - ogRow) + abs(nc - ogCol)
                        q.append([nr, nc, ogRow, ogCol])
            
            return mat
        

        mat = getMat()

        dists = [[float("-inf")] * n for _ in range(m)]

        dists[0][0] = mat[0][0]

        maxHeap = [[-mat[0][0], 0, 0]]

        while maxHeap:
            pathVal, r, c = heapq.heappop(maxHeap)
            pathVal *= - 1
            if pathVal < dists[r][c]:
                continue
            
            for dx, dy in dirs:
                nr = r + dx
                nc = c + dy
                if valid(nr, nc) and mat[nr][nc] != float("inf"):
                    newPath = min(pathVal, mat[nr][nc])
                    if newPath > dists[nr][nc]:
                        dists[nr][nc] = newPath
                        heapq.heappush(maxHeap, [-newPath, nr, nc])
        

        return dists[m - 1][n - 1] if dists[m - 1][n - 1] != float("-inf") else 0