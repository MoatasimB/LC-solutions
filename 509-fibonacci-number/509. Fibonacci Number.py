class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        oneBack = 1
        twoBack = 0

        for i in range(2, n+1):
            curr = oneBack + twoBack
            twoBack = oneBack
            oneBack = curr
        
        return oneBack
        
        
        if n == 0:
            return 0
        if n == 1:
            return 1
        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]


        dp = {}
        def dfs(n):
            if n == 1:
                return 1
            if n == 0:
                return 0
            if n in dp:
                return dp[n]
            
            dp[n]  = dfs(n-1) + dfs(n-2)
            return dp[n]
        
        return dfs(n)


