class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])

        def valid(r,c):
            return 0<=r<m and 0<=c<n and grid[r][c] == 0

        dirs = [(0,1), (1,0), (0,-1), (-1,0)]

        empty_spots = defaultdict(list)
        q = deque()
        seen = defaultdict(set)

        count = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    q.append((r,c,count, 0))
                    seen[count].add((r,c))
                    count += 1
        


        while q:
            r, c, id, dist = q.popleft()

            for dx, dy in dirs:
                nr = r + dx
                nc = c + dy

                if valid(nr, nc) and (nr,nc) not in seen[id]:
                    empty_spots[(nr,nc)].append(dist + 1)
                    q.append((nr,nc,id,dist + 1))
                    seen[id].add((nr,nc))

        
        ans = float('inf')
        for spot, dists in empty_spots.items():
            if len(dists) == count:
                ans = min(ans, sum(dists))
        

        return ans if ans != float('inf') else -1
