class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        n = len(s)
        dp = {}
        def dfs(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            if i==j:
                if s[i] == s[j]:
                    return 0
                else:
                    return 1
            if i > j:
                return 0

            ans = float('inf')
            if s[i] == s[j]:
                ans = dfs(i+1, j-1)
            else:
                ans = 1 + min(dfs(i+1, j), dfs(i, j-1))
            
            dp[(i,j)] = ans
            return ans

        return dfs(0, n-1) <= k


