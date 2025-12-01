class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        

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