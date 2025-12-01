class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        

        idx_map = {}
        l = 0
        ans = 0

        for r in range(len(s)):
            if s[r] in idx_map:
                l = max(l, idx_map[s[r]] + 1)
            
            ans = max(ans, r - l + 1)
            idx_map[s[r]] = r
        
        return ans

        
        
        freq = defaultdict(int)

        l = 0
        ans = 0



        for r in range(len(s)):
            ch = s[r]
            freq[ch] += 1

            while freq[ch] > 1:
                freq[s[l]] -= 1
                l += 1
            
            ans = max(ans, r - l + 1)
        
        return ans