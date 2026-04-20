class Solution:
    def colorGrid(self, n: int, m: int, sources: list[list[int]]) -> list[list[int]]:
        
        def valid(r, c):
            return 0 <= r < n and 0 <= c < m
        

        grid = [[0] * m for _ in range(n)]

        q = deque()
        
        for r, c, color in sources:
            grid[r][c] = color
            q.append([r, c, color])
        
        dirs = [(0, 1), (1,0), (0,-1), (-1,0)]

        while q:
            q_len = len(q)
            new = defaultdict(int)
            for _ in range(q_len):
                r, c, color = q.popleft()
                for dx, dy in dirs:
                    nr, nc = r + dx, c + dy
                    if valid(nr, nc) and grid[nr][nc] == 0:
                        new[(nr,nc)] = max(new[(nr, nc)], color)

            for key, val in new.items():
                nr, nc = key  
                grid[nr][nc] = val
                q.append([nr, nc, val])
        
        return grid