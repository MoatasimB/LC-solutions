class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        

        ans = []

        def dfs(left, right, curr):

            if left == n and right == n:
                ans.append("".join(curr[:]))
                return
            
            if left < n:
                curr.append("(")
                dfs(left + 1, right, curr)
                curr.pop()
            
            if right < left:
                curr.append(")")
                dfs(left, right + 1, curr)
                curr.pop()
            
        dfs(0,0,[])
        return ans