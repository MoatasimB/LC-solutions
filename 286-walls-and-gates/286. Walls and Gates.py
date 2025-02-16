class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        
        q = deque()
        seen = set()
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        def valid(r, c):
            return 0<= r < len(rooms) and 0<= c < len(rooms[0])
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    q.append((i,j, 0))
                    seen.add((i,j))
        
        while q:
            row, col, dist = q.popleft()

            for dx, dy in dirs:
                nr, nc = row + dx, col + dy

                if valid(nr,nc) and (nr, nc) not in seen and rooms[nr][nc] != -1:
                    rooms[nr][nc] = dist + 1
                    q.append((nr, nc, dist + 1))
                    seen.add((nr, nc))
        
