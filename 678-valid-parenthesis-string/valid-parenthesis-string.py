class Solution:
    def checkValidString(self, s: str) -> bool:
        #i x left
        dp = [[False] * (len(s) + 1) for _ in range(len(s) + 1)]

        dp[len(s)][0] = True
        for i in range(len(s) - 1, -1, -1):
            for left in range(len(s)):
                ans = False
                if s[i] == "(":
                    if dp[i+1][left + 1]:
                        ans = True
                elif s[i] == ")":
                    if left > 0 and dp[i+1][left - 1]:
                        ans = True
                #skip, left, right
                else:
                    if dp[i + 1][left]:
                        ans = True
                    if left < len(s) and dp[i + 1][left + 1]:
                        ans = True
                    if left > 0 and dp[i + 1][left - 1]:
                        ans = True
                dp[i][left] = ans
        return dp[0][0]
        # dp = {}
        # def dfs(i, left):
        #     if i == len(s):
        #         return True if left == 0 else False
        #     if (i, left) in dp:
        #         return dp[(i,left)]
        #     if left < 0:
        #         return False
        #     ans = False
        #     if s[i] == "(":
        #         if dfs(i+1, left + 1):
        #             ans = True
        #     elif s[i] == ")":
        #         if dfs(i+1, left - 1):
        #             ans = True
        #     #skip, left, right
        #     else:
        #         if dfs(i + 1, left) or dfs(i + 1, left + 1) or dfs(i + 1, left -1):
        #             ans = True
        #     dp[(i,left)] = ans
        #     return ans
        
        # return dfs(0,0)
            