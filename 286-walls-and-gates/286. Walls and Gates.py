class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        

        q = deque()

        m = len(rooms)
        n = len(rooms[0])
        def valid(r, c):
            return 0 <= r < m and 0 <= c < n
        
        dirs = [(0, 1), (1,0), (0,-1), (-1,0)]

        for r in range(m):
            for c in range(n):
                if rooms[r][c] == 0:
                    q.append([0, r, c])
                    rooms[r][c] = 0
        
        while q:
            dist, r, c = q.popleft()

            for dx, dy in dirs:
                nr = r + dx
                nc = c + dy
                if valid(nr, nc) and rooms[nr][nc] == 2147483647:
                    q.append([dist + 1, nr, nc])
                    rooms[nr][nc] = dist + 1
        
        
    
        
                    