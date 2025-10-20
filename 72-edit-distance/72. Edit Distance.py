class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        
        n = len(word1)
        m = len(word2)

        dp = [[0] * (m+1) for _ in range(n+1)]

        for j in range(1, m+1):
            dp[0][j] = j
        for i in range(1, n+1):
            dp[i][0] = i
        
        
        for i in range(1, n+1):
            for j in range(1, m+1):
                ans = 0
                if word1[i-1] == word2[j-1]:
                    ans = dp[i-1][j-1]
                else:
                    ans =  1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                dp[i][j] = ans
        return dp[n][m]
        
        memo = {}
        def dfs(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            if i == 0 and j == 0:
                return 0
            if i == 0:
                return j
            if j == 0:
                return i
            ans = 0
            if word1[i-1] == word2[j-1]:
                ans = dfs(i-1, j-1) 
            else:
                ans =  1 + min(dfs(i-1, j), dfs(i, j-1), dfs(i-1,j-1))
            memo[(i,j)] = ans
            return ans
        
        return dfs(n, m)

        