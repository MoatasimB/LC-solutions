class Solution:
    def numDecodings(self, s: str) -> int:
        
        dp = {}
        def dfs(i):

            if i == len(s):
                return 1
            if i in dp:
                return dp[i]
            
            ans = 0
            #take 1
            if s[i] != '0':
                ans += dfs(i+1)

            #take 2
            if i < len(s) - 1 and s[i] != '0' and  int(s[i:i+2]) <= 26:
                ans += dfs(i+2)

            dp[i] = ans
            return ans
        
        return dfs(0)
