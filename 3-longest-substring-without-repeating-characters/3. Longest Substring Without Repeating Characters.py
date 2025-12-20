class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        last = {}

        l = 0
        ans = 0
        for r in range(len(s)):
            if s[r] in last:
                l = max(l, last[s[r]] + 1)
            
            ans = max(ans, r - l + 1)
            last[s[r]] = r
        
        return ans