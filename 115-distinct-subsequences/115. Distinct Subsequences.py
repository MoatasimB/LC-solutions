class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
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
        m = len(s)
        n = len(t)
        return dfs(m - 1, n - 1)