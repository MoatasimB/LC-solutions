class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        ans = []
        def dfs(i, left, right, curr):

            # if i == len(s) and left == right:
            #     ans.append("".join(curr[:]))
            #     return
            while i<len(s) and s[i] != "(" and s[i] != ")":
                curr.append(s[i])
                i += 1
            
            if i == len(s):
                if left == right:
                    ans.append("".join(curr[:]))
                return

            if s[i] == "(":
                dfs(i+1, left + 1, right, curr + ["("])
            else:
                if left > right:
                    dfs(i+1, left, right + 1, curr + [")"])
            
            #skip
            dfs(i+1, left, right, curr)
        
        dfs(0,0,0, [])
        longest = max(len(x) for x in ans)
        ans = set(ans)
        final = [x for x in ans if len(x) == longest]
        return final