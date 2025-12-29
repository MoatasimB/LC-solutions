class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        memo = {}
        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i == len(s) and j == len(p):
                return True
            if j == len(p):
                return False
            
            isMatch = (i < len(s) and (s[i] == p[j] or p[j] == "."))

            memo[(i, j)] = False
            if j + 1 < len(p) and p[j + 1] == "*":
                # memo[(i, j)] = (isMatch and dfs(i + 1, j)) or dfs(i, j + 2)
                if isMatch:
                    if dfs(i + 1, j):
                        memo[(i, j)] = True
                        return True
                if dfs(i, j + 2):
                    memo[(i, j)] = True
                    return True
            if isMatch and dfs(i + 1, j + 1):
                memo[(i, j)] = True
                return True
            
            return memo[(i, j)]
        
        return dfs(0, 0)