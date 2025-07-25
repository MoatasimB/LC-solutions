class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        

        dirs = [(0,1), (0,-1), (1,0), (-1,0)]

        m = len(maze)
        n = len(maze[0])

        def valid(r,c):
            return 0<=r<m and 0<=c<n and maze[r][c] == 0
        
        pq = [[0, start[0], start[1]]] #dist, r, c
        distance = {(i,j): float('inf') for i in range(m) for j in range(n)}
        distance[(start[0],start[1])] = 0
        while pq:
            dist, r, c = heapq.heappop(pq)

            for dx, dy in dirs:
                curr = 0
                nr = r + dx
                nc = c + dy
                if not valid(nr,nc):
                    continue
                while valid(nr,nc):
                    curr += 1
                    nr += dx
                    nc += dy
                nr -= dx
                nc -= dy

                if distance[(nr,nc)] > dist + curr:
                    distance[(nr,nc)] = dist + curr
                    heapq.heappush(pq, [dist + curr, nr, nc])

        return distance[(destination[0], destination[1])] if distance[(destination[0], destination[1])] != float('inf') else -1 