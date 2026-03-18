class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        
    
        m = len(grid)
        n = len(grid[0])
        ans = 0
        for r in range(m):
            for c in range(n):
                diag = grid[r - 1][c - 1] if r - 1 >= 0 and c - 1 >= 0 else 0
                up = grid[r - 1][c] if r - 1 >= 0 else 0
                left = grid[r][c - 1] if c - 1 >= 0 else 0

                grid[r][c] += left + up - diag
                if grid[r][c] <= k:
                    ans += 1
        
        return ans