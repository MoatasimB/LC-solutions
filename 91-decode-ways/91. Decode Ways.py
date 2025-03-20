class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        dp[len(s)] = 1

        for i in range(len(s) - 1, - 1, -1):
            ans = 0
            if s[i] != '0':
                ans += dp[i + 1]
            if i < len(s) - 1 and s[i] != '0' and  int(s[i:i+2]) <= 26:
                ans += dp[i + 2]
            dp[i] = ans
        
        return dp[0]
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
