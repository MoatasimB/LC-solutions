class Solution:
    def checkValidString(self, s: str) -> bool:
        dp = {}
        def dfs(i, left, right):
            if i == len(s):
                return True if left == right else False
            if (i, left, right) in dp:
                return dp[(i,left,right)]
            if right > left:
                return False
            ans = False
            if s[i] == "(":
                if dfs(i+1, left + 1, right):
                    ans = True
            elif s[i] == ")":
                if dfs(i+1, left, right + 1):
                    ans = True
            #skip, left, right
            else:
                if dfs(i + 1, left, right) or dfs(i + 1, left + 1, right) or dfs(i + 1, left, right + 1):
                    ans = True
            dp[(i,left, right)] = ans
            return ans
        
        return dfs(0,0,0)
            