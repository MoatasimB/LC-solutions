class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        
        m = len(grid)
        n = len(grid[0])
        
        prefix = 1
        ans = [[1] * n for _ in range(m)]
        for r in range(m):
            for c in range(n):
                ans[r][c] = prefix
                prefix = (prefix * grid[r][c]) % 12345

                
        suffix = 1
        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                ans[r][c] = (ans[r][c] * suffix) % 12345
                suffix = (suffix * grid[r][c]) % 12345
                  
                
        
        return ans

        # 1 2 6 12

        # 1   2   12 144
        # 144 144 72  12
        

        [144, 72, 24, 1]

        [1, 1, 2, 12]
