class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        new_p = []

        for ch in p:
            if not new_p or ch != "*":
                new_p.append(ch)
            elif new_p[-1] != "*":
                new_p.append(ch)
        memo = {}

        def dfs(s, p):

            if (s,p) in memo:
                return memo[(s,p)]
            
            memo[(s,p)] = False
            if s == p or p == "*":
                memo[(s,p)] = True
            elif s == "" or p == "":
                memo[(s,p)] = False
            elif s[0] == p[0] or p[0] == "?":
                memo[(s,p)] = dfs(s[1:], p[1:])
            elif p[0] == "*":
                memo[(s,p)] = dfs(s[1:], p) or dfs(s, p[1:])
            
            return memo[(s,p)]
        

        return  dfs(s, "".join(new_p))


   