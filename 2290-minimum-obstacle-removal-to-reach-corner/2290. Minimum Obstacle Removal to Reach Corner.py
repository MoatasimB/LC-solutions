class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])

        def valid(r, c):
            return 0<= r < m and 0 <= c < n
        
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        seen = set()
        q = deque()

        seen.add((0,0))
        q.append([0, 0, 0])

        while q:
            r, c, cost = q.popleft()

            if (r, c) == (m - 1, n - 1):
                return cost

            for dx, dy in dirs:
                nr = r + dx
                nc = c + dy
                if valid(nr, nc) and (nr, nc) not in seen:
                    seen.add((nr, nc))
                    if grid[nr][nc] == 1:
                        q.append([nr, nc, cost + 1])
                    else:
                        q.appendleft([nr, nc, cost])

