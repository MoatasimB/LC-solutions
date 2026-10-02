class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        
        ans = []

        def dfs(curr, count):
            if len(curr) == 2 * n:
                if count == 0:
                    ans.append("".join(curr[:]))
                return
            
            dfs(curr + ["("], count + 1)
            if count > 0:
                dfs(curr + [")"], count - 1)
        
        dfs([], 0)
        return ans
