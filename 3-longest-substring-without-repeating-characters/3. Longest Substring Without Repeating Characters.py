class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        mpp = defaultdict(int)

        l = 0
        ans = 0
        for r in range(len(s)):
            mpp[s[r]] += 1

            while mpp[s[r]] > 1:
                mpp[s[l]] -= 1
                l += 1
            
            ans = max(ans, r - l + 1)
        
        return ans