class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        def valid(r,c):
            return 0<=r<m and 0<=c<n
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        
        ans = float("inf")
        heap = [[-grid[0][0], 0, 0]] #cell val, r,c
        seen = [[False] * n for _ in range(m)]
        while heap:
            cell_val, r, c = heapq.heappop(heap)
            ans = min(ans, -cell_val)
            if r == m - 1 and c == n - 1:
                return ans
            
            seen[r][c] = True

            for dx, dy in dirs:
                nr, nc = r + dx, c + dy
                if valid(nr,nc) and not seen[nr][nc]:
                    heapq.heappush(heap, [-grid[nr][nc], nr, nc])
