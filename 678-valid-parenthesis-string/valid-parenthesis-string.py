class Solution:
    def checkValidString(self, s: str) -> bool:
        dp = {}
        def dfs(i, left):
            if i == len(s):
                return True if left == 0 else False
            if (i, left) in dp:
                return dp[(i,left)]
            if left < 0:
                return False
            ans = False
            if s[i] == "(":
                if dfs(i+1, left + 1):
                    ans = True
            elif s[i] == ")":
                if dfs(i+1, left - 1):
                    ans = True
            #skip, left, right
            else:
                if dfs(i + 1, left) or dfs(i + 1, left + 1) or dfs(i + 1, left -1):
                    ans = True
            dp[(i,left)] = ans
            return ans
        
        return dfs(0,0)
            