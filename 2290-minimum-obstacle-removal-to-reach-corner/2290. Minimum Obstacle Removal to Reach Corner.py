class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        
        dirs = [(0, 1), (1,0), (0,-1), (-1,0)]

        def valid(r, c):
            return 0<= r < m and 0<= c <n
        
        dists = [[float("inf")] * n for _ in range(m)]

        dists[0][0] = 0

        minHeap = [[0, 0, 0]] #cost, r, c

        while minHeap:
            cost, r, c = heapq.heappop(minHeap)

            if dists[r][c] < cost:
                continue
            if r == m - 1 and c == n - 1:
                return cost
            for dx, dy in dirs:
                nr = r + dx
                nc = c + dy

                if valid(nr, nc):
                    newCost = 1 + cost if grid[nr][nc] == 1 else cost
                    if dists[nr][nc] > newCost:
                        dists[nr][nc] = newCost
                        heapq.heappush(minHeap, [newCost, nr, nc])
                   
        