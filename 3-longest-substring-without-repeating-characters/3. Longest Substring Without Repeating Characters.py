class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        unique = set()
        left = 0
        ans = 0

        for right in range(len(s)):
            while s[right] in unique:
                unique.remove(s[left])
                left += 1

            unique.add(s[right])
            window_size = right - left + 1
            ans = max(ans, window_size)

        return ans