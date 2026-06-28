class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7

        dp = [[[0]* (r - l + 1) for _ in range(2)] for _ in range(n)]
        for val in range(r - l + 1):
            dp[0][0][val] = 1
            dp[0][1][val] = 1
        
        for i in range(1, n):
            prefix = 0
            for val in range(r - l + 1):
                dp[i][0][val] = prefix
                prefix += (dp[i - 1][1][val] % MOD) % MOD
            suffix = 0
            for val in range(r -l, -1, -1):
                dp[i][1][val] = suffix
                suffix += (dp[i - 1][0][val] % MOD) % MOD
                
                
        ans = 0

        for i in range(r - l + 1):
            ans += dp[n-1][0][i] % MOD
            ans += dp[n-1][1][i] % MOD
        return ans % MOD
        #up down
        memo = {}
        # I am going up so prev must be greater than me (and not equal)
        # I am going down so prev must be less than me (and not equal)
        def dfs(i, d, val):
            if i == -1:
                return 1
            if (i, d, val) in memo:
                return memo[(i, d, val)]
            curr = 0

            if d == 0:
                for num in range(l, val):
                    curr += dfs(i - 1, 1, num) % MOD
            else:
                for num in range(val + 1, r + 1):
                    curr += dfs(i - 1, 0, num) % MOD
   
            memo[(i, d, val)] = curr % MOD
            return curr % MOD
        
        ans = 0

        for i in range(l, r + 1):
            ans += dfs(n - 2, 0, i) % MOD
            ans += dfs(n - 2, 1, i) % MOD     
        return ans % MOD

        