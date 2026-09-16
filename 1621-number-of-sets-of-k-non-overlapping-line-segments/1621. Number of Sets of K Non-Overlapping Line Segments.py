class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        
        dp = [[[0] * 2 for _ in range(k + 1)] for _ in range(n + 1)]
        for i in range(n + 1):
            for m in range(2):
                dp[i][0][m] = 1
        
        for i in range(n - 1, -1, -1):
            for j in range(1, k + 1):
                for p in range(2):
                    ans = 0
                    ans += dp[i + 1][j][1]
                    #if we have a starting point
                    if p:
                        #or we can decide to end it and go to the next state
                        ans += dp[i][j - 1][0]
                    if not p:
                        #we can continue to skip
                        ans += dp[i + 1][j][0]
                    dp[i][j][p] = ans % (10**9 + 7)
        return dp[0][k][0] % (10**9 + 7)
        
        memo = {}
        def dfs(i, count, placed):
            if (i, count, placed) in memo:
                return memo[(i, count, placed)]
            if count == 0:
                return 1
            if i == n:
                return 0
            ans = 0
            #if we have a starting point
            if placed:
                #we can continue on
                ans += dfs(i + 1, count, True)
                #or we can decide to end it and go to the next state
                ans += dfs(i, count - 1, False)
            
            if not placed:
                #we can place
                ans += dfs(i + 1, count, True)
                #we can continue to skip
                ans += dfs(i + 1, count, False)
            
            
            memo[(i, count, placed)] = ans %  (10**9 + 7) 
            return ans %  (10**9 + 7) 
        return dfs(0, k, False) % (10**9 + 7) 
        