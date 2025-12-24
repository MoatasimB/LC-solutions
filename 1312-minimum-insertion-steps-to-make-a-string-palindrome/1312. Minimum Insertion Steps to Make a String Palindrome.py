class Solution:
    def minInsertions(self, s: str) -> int:
        
        n = len(s)
        s2 = s[::-1]

        prev = [0] * (n + 1)

        for i in range(1, n + 1):
            curr = [0] * (n + 1)
            for j in range(1, n + 1):
                if s[i - 1] == s2[j - 1]:
                    curr[j] = 1 + prev[j - 1]
                else:
                    curr[j] = max(prev[j], curr[j - 1])
            prev = curr

        LCS = prev[n]

        return n - LCS

        # memo = {}
        # def dfs(i, j):
        #     if (i, j) in memo:
        #         return memo[(i, j)]
        #     if i == -1 or j == -1:
        #         return 0

        #     ans = 0
        #     if s[i] == s2[j]:
        #         ans = 1 + dfs(i - 1, j - 1)
        #     else:
        #         ans = max(dfs(i - 1, j), dfs(i, j - 1))

        #     memo[(i, j)] = ans
        #     return ans
        
        # LCS = dfs(n - 1, n - 1)
        # return n - LCS
