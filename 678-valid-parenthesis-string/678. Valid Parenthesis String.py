class Solution:
    def checkValidString(self, s: str) -> bool:
        
        memo = {}
        def dfs(i, left):
            if (i, left) in memo:
                return memo[(i, left)]
            if i == len(s):
                return left == 0
            if left < 0:
                return False

            ch = s[i]

            if ch == "(":
                if dfs(i + 1, left + 1):
                    memo[(i, left)] = True
                    return True
            elif ch == ")":
                if dfs(i + 1, left - 1):
                    memo[(i, left)] = True
                    return True
            else:
                if dfs(i + 1, left + 1) or dfs(i + 1, left - 1) or dfs(i + 1, left):
                    memo[(i, left)] = True
                    return True
            memo[(i, left)] = False
            return False
        
        return dfs(0, 0)