class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        n = len(s)
        if not s:
            return 0

        l = 0
        last = {}
        ans = float("-inf")
        for r in range(n):
            if s[r] in last:
                l = max(l, last[s[r]] + 1)
            ans = max(ans, r - l + 1)
            last[s[r]] = r
        
        return ans
