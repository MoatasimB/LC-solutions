class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        new_p = []
        
        for ch in p:
            if not new_p:
                new_p.append(ch)
            elif ch == "*":
                if new_p[-1] != "*":
                    new_p.append(ch)
            else:
                new_p.append(ch)
        
        p = "".join(new_p)
        memo = {}
        def dfs(i, j):
            if (i,j) in memo:
                return memo[(i,j)]
            if (i == len(s) and j == len(p)) or (i == len(s) and p[j:] == "*"):
                return True
            # if i == len(s) and (p[j] == "*" and j == len(p) - 1):
            #     return True
            if j == len(p) or i == len(s):
                return False
            
            
            if s[i] == p[j] or p[j] == "?":
                memo[(i,j)] = dfs(i+1, j+1)
                return memo[(i,j)]
            
            if p[j] == "*":
                memo[(i,j)] = dfs(i+1, j) or dfs(i, j+1)
                return memo[(i,j)]

            
            memo[(i,j)] = False
            return False
        
        return dfs(0,0)
    

        