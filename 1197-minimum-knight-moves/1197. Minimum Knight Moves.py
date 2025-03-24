class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        
        dirs = [(-2,1), (-1,2), (1,2), (2,1), (2,-1), (1,-2), (-1,-2), (-2,-1)]

        q = deque()
        seen = set()

        q.append((0,0, 0))
        seen.add((0,0))

        while q:
            r,c,cost = q.popleft()

            if (r,c) == (x,y):
                return cost

            for dx, dy in dirs:
                nr, nc = r + dx, c + dy

                if (nr,nc) not in seen:
                    seen.add((nr,nc))
                    q.append((nr,nc, cost + 1))
        
        