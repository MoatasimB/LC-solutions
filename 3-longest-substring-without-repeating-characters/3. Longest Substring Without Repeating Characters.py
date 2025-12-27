class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        n = len(s)
        if not s:
            return 0

        l = 0
        freq = defaultdict(int)
        ans = float("-inf")
        for r in range(n):
            freq[s[r]] += 1

            while freq[s[r]] > 1:
                freq[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
        
        return ans
