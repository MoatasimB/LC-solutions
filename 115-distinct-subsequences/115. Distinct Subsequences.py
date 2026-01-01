class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)
        prev = [0] * (n + 1)

        prev[0] = 1
        
        for i in range(1, m + 1):
            curr = [0] * (n + 1)
            curr[0] = 1
            for j in range(1, n + 1):

                if s[i - 1] == t[j - 1]:
                    curr[j] = prev[j - 1] + prev[j]
                else:
                    curr[j] = prev[j]
            prev = curr
        
        return prev[n]
        
        return dp[m][n]


        memo = {}
        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if j == -1:
                return 1
            if i == -1:
                return 0
            
            ans = 0

            if s[i] == t[j]:
                ans += dfs(i - 1, j - 1) + dfs(i - 1, j)
            else:
                ans += dfs(i - 1, j)
            
            memo[(i, j)] = ans
            return ans
        
        return dfs(m - 1, n - 1)