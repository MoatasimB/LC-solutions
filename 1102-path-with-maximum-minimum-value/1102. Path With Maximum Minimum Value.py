class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        def valid(r,c):
            return 0<=r<m and 0<=c<n
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        
        def check(mid):
            if grid[0][0] < mid:
                return False
            seen = set()
            seen.add((0,0))
            def dfs(r, c):
                if r == m - 1 and c == n - 1:
                    return True
                for dx, dy in dirs:
                    nr, nc = r + dx, c + dy
                    if valid(nr,nc) and (nr,nc) not in seen and grid[nr][nc] >= mid:
                        seen.add((nr,nc))
                        if dfs(nr,nc):
                            return True
                return False
            return dfs(0,0)

        
        
        
        l = min([min(row) for row in grid])
        r = max([max(row) for row in grid])
        ans = l
        while l <= r:
            mid = (l + r) // 2

            if check(mid):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        
        return ans
