class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        
        l = 0
        counts = [0] * 3
        ans = 0

        for r in range(len(s)):

            counts[ord(s[r]) - ord('a')] += 1

            while counts[0] and counts[1] and counts[2]:
                ans += len(s) - r
                counts[ord(s[l]) - ord('a')] -= 1
                l += 1
        
        return ans

