class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        
        m = len(rooms)
        n = len(rooms[0])

        dirs = [(0,1), (1,0), (0,-1), (-1,0)]

        def valid(r,c):
            return 0<=r<m and 0<=c<n and rooms[r][c] == 2147483647
        
        q = deque()
        seen = set()
        for r in range(m):
            for c in range(n):
                if rooms[r][c] == 0:
                    q.append((r,c,0))
                    seen.add((r,c))
        
        while q:
            r, c, dist = q.popleft()

            for dx, dy in dirs:
                nr = r + dx
                nc = c + dy
                if valid(nr, nc) and (nr,nc) not in seen:
                    rooms[nr][nc] = dist + 1
                    q.append((nr,nc,dist + 1))
                    seen.add((nr,nc))
        
        return rooms
