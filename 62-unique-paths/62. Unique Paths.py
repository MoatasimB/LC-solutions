class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        for r in range(m):
            for c in range(n):
                if r == 0 and c == 0:
                    continue
                left = 0
                up = 0
                if r - 1 >= 0:
                    up = dp[r-1][c]
                if c - 1 >= 0:
                    left = dp[r][c - 1]
                dp[r][c] = left + up
        
        return dp[m - 1][n - 1]
        
        memo = {}
        def dfs(r, c):
            if (r, c) in memo:
                return memo[(r, c)]
            if r == 0 and c == 0:
                return 1
            
            if r < 0 or c < 0:
                return 0
            
            left = dfs(r, c - 1)
            up = dfs(r - 1, c)

            memo[(r, c)] = left + up
            return left + up
        
        return dfs(m - 1, n - 1)
