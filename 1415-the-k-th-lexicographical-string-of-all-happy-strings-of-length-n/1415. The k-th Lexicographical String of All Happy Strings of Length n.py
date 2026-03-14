class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        
        chs = "abc"

        def backtrack(curr):

            if len(ans) == k:
                return

            if len(curr) == n:
                ans.append("".join(curr[:]))
                return
            
            for ch in chs:
                if curr and curr[-1] == ch:
                    continue
                
                curr.append(ch)
                backtrack(curr)
                curr.pop()
        
        ans = []
        backtrack([])
        if len(ans) < k:
            return ""
        
        return ans[k-1]
