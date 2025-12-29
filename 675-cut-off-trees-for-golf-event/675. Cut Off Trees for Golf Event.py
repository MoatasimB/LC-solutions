class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        
        m = len(forest)
        n = len(forest[0])

        def valid(r, c):
            return 0<= r < m and 0<=c<n
        
        dirs = [(0, 1), (1,0), (0,-1), (-1,0)]


        def bfs(startR, startC, targetR, targetC):
            q = deque()
            seen = set()

            q.append([startR, startC, 0])
            seen.add((startR, startC))

            while q:
                r, c, steps = q.popleft()

                if (r, c) == (targetR, targetC):
                    return steps
                
                for dx, dy in dirs:
                    nr = r + dx
                    nc = c + dy
                    if valid(nr, nc) and (nr, nc) not in seen and forest[nr][nc] != 0:
                        q.append([nr, nc, steps + 1])
                        seen.add((nr,nc))
            
            return -1
        

        cellsToCut = [[forest[r][c], r, c] for r in range(m) for c in range(n) if forest[r][c] > 1]

        cellsToCut.sort()

        if forest[0][0] == 0:
            return -1
        
        startR = 0
        startC = 0
        total = 0
        for val, r, c in cellsToCut:
            curr = bfs(startR, startC, r, c)
            if curr == -1:
                return -1
            
            total += curr
            startR = r
            startC = c
        
        return total
            
