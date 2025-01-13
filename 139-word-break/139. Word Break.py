class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        dp = {}
        def dfs(i):

            if s[i:] in wordDict:
                return True
            # if i == len(s):
            #     return False
            if i in dp:
                return dp[i]
            for j in range(i, len(s)):
                if s[i:j+1] in wordDict:
                    if dfs(j+1):
                        dp[i] = True
                        return True
            dp[i] = False
            return False
        return dfs(0)
