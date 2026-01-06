class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        #path sum -> largest value we've seen so far in our path
        m = len(grid)
        n = len(grid[0])

        def valid(r, c):
            return 0 <= r < m and 0 <= c < n
        
        dirs = [(0, 1), (1,0), (0,-1), (-1,0)]


        dists = [[float("inf")] * n for _ in range(m)] #time to reach this cell

        dists[0][0] = grid[0][0]

        minHeap = [[grid[0][0], 0, 0]] #[pathSum, r, c]

        while minHeap:
            pathVal, r, c = heapq.heappop(minHeap)

            if dists[r][c] < pathVal:
                continue
            
            if (r, c) == (m - 1, n - 1):
                return pathVal
            
            for dx, dy in dirs:
                nr = r + dx
                nc = c + dy

                if valid(nr, nc):
                    newVal = max(grid[nr][nc], pathVal)
                    if dists[nr][nc] > newVal:
                        dists[nr][nc] = newVal
                        heapq.heappush(minHeap, [newVal, nr, nc])
        
