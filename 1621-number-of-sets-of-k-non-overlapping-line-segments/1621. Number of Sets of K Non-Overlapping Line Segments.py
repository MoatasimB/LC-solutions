class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        
        dp = [[[0] * 2 for _ in range(k)] for _ in range(n)]
        for i in range(n):
            for m in range(2):
                dp[i][0][m] = 1
        
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
        