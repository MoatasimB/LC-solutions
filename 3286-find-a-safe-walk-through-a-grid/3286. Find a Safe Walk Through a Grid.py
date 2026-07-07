class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        
        m = len(grid)
        n = len(grid[0])

        minHeap = [[grid[0][0], 0, 0]] #pathCost, r, c
        dists = [[float("inf")] * n for _ in range(m)]
        dists[0][0] = grid[0][0]
        dirs = [(0, 1), (1,0), (0,-1), (-1,0)]
        def valid(r, c):
            return 0 <= r < m and 0 <= c < n

        while minHeap:
            pathCost, r, c = heapq.heappop(minHeap)

            if pathCost > dists[r][c]:
                continue
                
            if (r, c) == (m - 1, n - 1):
                return pathCost < health
            
            for dx, dy in dirs:
                nr, nc = r + dx, c + dy
                if valid(nr, nc):
                    newPath = grid[nr][nc] + pathCost
                    if newPath < dists[nr][nc]:
                        dists[nr][nc] = newPath
                        heapq.heappush(minHeap, [newPath, nr, nc])
                    
        
