class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        freq = defaultdict(int)

        l = 0
        maxF = 0
        ans = 0
        for r in range(len(s)):
            freq[s[r]] += 1
            if freq[s[r]] > maxF:
                maxF = freq[s[r]]
            
            while (r - l + 1) - maxF > k:
                freq[s[l]] -= 1
                l += 1
                # maxF = 0
                # for val in freq.values():
                #     maxF = max(maxF, val)
            
            ans = max(ans, r - l + 1)

        return ans
