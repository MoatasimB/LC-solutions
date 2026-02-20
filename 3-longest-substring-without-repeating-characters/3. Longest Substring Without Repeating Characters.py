class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        unique = {}
        left = 0
        ans = 0

        for right in range(len(s)):
            if s[right] in unique:
                if left <= unique[s[right]]:
                    left = unique[s[right]] + 1
                unique[s[right]] = right
                window_size = right - left + 1
                ans = max(ans, window_size)
            else:
                unique[s[right]] = right
                window_size = right - left + 1
                ans = max(ans, window_size)

        return ans
