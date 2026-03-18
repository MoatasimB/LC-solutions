class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        
    
        m = len(grid)
        n = len(grid[0])
        mat = [[0] * n for _ in range(m)]
        ans = 0
        for r in range(m):
            for c in range(n):
                diag = mat[r - 1][c - 1] if r - 1 >= 0 and c - 1 >= 0 else 0
                up = mat[r - 1][c] if r - 1 >= 0 else 0
                left = mat[r][c - 1] if c - 1 >= 0 else 0

                mat[r][c] = left + up + grid[r][c] - diag
                if mat[r][c] <= k:
                    ans += 1
        
        return ans