class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}
        def dfs(n):
            if n == 1 or n == 0:
                return 1
            if n < 0:
                return 0
            
            if n in dp:
                return dp[n]
            one = dfs(n-1)
            two = dfs(n-2)
            dp[n] = one + two
            return  dp[n]
        
        return dfs(n)