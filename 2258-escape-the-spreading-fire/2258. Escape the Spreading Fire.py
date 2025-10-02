class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def valid(r,c):
            return 0<=r<m and 0<=c<n
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        
        fire_time_grid = {}
        q = deque()
        seen = set()

        for r in range(m):
            for c in range(n):
                fire_time_grid[(r,c)] = float("inf")
                if grid[r][c] == 1:
                    q.append((r,c,0))
                    seen.add((r,c))
                    fire_time_grid[(r,c)] = 0
        
        while q:
            r,c,time = q.popleft()

            for dx, dy in dirs:
                nr,nc = r + dx, c + dy
                if valid(nr,nc) and (nr,nc) not in seen and grid[nr][nc] == 0:
                    q.append((nr,nc,time + 1))
                    fire_time_grid[(nr,nc)] = time + 1
                    seen.add((nr,nc))
        
        def check(mid):
            q = deque()
            seen = set()

            q.append((0,0,mid)) #r,c,time to cell
            seen.add((0,0))

            while q:
                r,c,time = q.popleft()
                if ((r,c) == (m-1,n-1)) and fire_time_grid[(r,c)] >= time:
                    return True
                if fire_time_grid[(r,c)] <= time:
                    continue
                for dx, dy in dirs:
                    nr,nc = r + dx, c + dy
                    if valid(nr,nc) and (nr,nc) not in seen and grid[nr][nc] == 0:
                        q.append((nr,nc,time + 1))
                        seen.add((nr,nc))
            return False
        print(fire_time_grid)
        l = 0
        r = 10**9
        ans = -1
        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                ans = max(ans,mid)
                l = mid + 1
            else:
                r = mid - 1
        
        return ans

        # [[X,2,1,1,1],
        #  [X,2,1,2,2],
        #  [X,2,1,1,1],
        #  [X,X,2,2,1],
        #  [X,X,X,X,0]]



