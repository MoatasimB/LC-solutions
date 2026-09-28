class Solution:
    def maxDepth(self, s: str) -> int:
        
        open = 0
        ans = 0
        for i, ch in enumerate(s):
            if ch == "(":
                open += 1
            elif ch == ")":
                open -= 1
            ans = max(open, ans)
        return ans