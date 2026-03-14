class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        ans = []
        def dfs(curr):
            if len(ans) == k:
                return
            if len(curr) == n:
                ans.append(curr[:])
                return
            for letter in "abc":
                if not curr or curr[-1] != letter:
                    curr.append(letter)
                    dfs(curr)
                    curr.pop()
            if len(ans) == k:
                return 
                
        
        dfs([])
        print(ans)
        return "".join(ans[-1]) if len(ans) == k else ""

