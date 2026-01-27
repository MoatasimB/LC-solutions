class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        

        m = len(maze)
        n = len(maze[0])

        dirs = [(0, 1), (1, 0), (0,-1), (-1,0)]

        def valid(r, c):
            return 0 <= r < m and 0 <= c < n and maze[r][c] == 0
        
        def nextPos(r, c, direction):
            dx, dy = direction
            cost = 0
            while valid(r + dx, c + dy):
                r += dx
                c += dy
                cost += 1
            
            return [r, c, cost]
        
        sr, sc = start
        minHeap = [[0, sr, sc]]
        dists = [[float("inf")] * n for _ in range(m)]
        dists[sr][sc] = 0

        while minHeap:
            dist, r, c = heapq.heappop(minHeap)

            if [r, c] == destination:
                return dist
            
            if dists[r][c] < dist:
                continue
            
            for direction in dirs:
                nr, nc, cost = nextPos(r, c, direction)
                if dist + cost < dists[nr][nc]:
                    dists[nr][nc] = dist + cost
                    heapq.heappush(minHeap, [dist + cost, nr, nc])
        

        return -1

