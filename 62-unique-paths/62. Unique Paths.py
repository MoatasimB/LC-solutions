class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        prev = [1] * n

        for i in range(1,m):
            curr = [0] * n
            for j in range(n):
         
                up = prev[j]
                left = 0
                if j > 0:
                    left = curr[j-1]
        
                curr[j] = up + left
            prev = curr
        
        return prev[n-1]
        
        
        
        dp = [[0]*n for _ in range(m)]

        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]




        return math.comb(m+n-2, m-1)
        
        
        
        dp = [[-1]*n for _ in range(m)]

        def dfs(i,j):
            if i == 0 and j == 0:
                return 1
            if i<0 or j<0:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            up = dfs(i-1,j)
            left = dfs(i,j-1)
            dp[i][j] = up + left
            return dp[i][j]
        
        return dfs(m-1,n-1)