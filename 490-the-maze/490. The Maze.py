class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        
        m = len(maze)
        n = len(maze[0])

        def valid(r, c):
            return 0 <= r < m and 0 <= c < n and maze[r][c] == 0
        
        dirs = [(0, 1), (1,0), (0,-1), (-1,0)]

        def nextPos(r, c, direction):
            dx, dy = direction

            while valid(r + dx, c + dy):
                r += dx
                c += dy

            
            return [r, c]
        
        q = deque()
        seen = set()

        sR, sC = start
        q.append([sR, sC])
        seen.add((sR, sC))

        while q:
            r, c = q.popleft()
            
            if [r, c] == destination:
                return True

            for direction in dirs:
                nr, nc = nextPos(r, c, direction)
                if (nr, nc) not in seen:
                    seen.add((nr, nc))
                    q.append([nr, nc])
        
        return False