class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        m = len(needle)
        n = len(haystack)
        index = 0
        for start in range(n-m+1):
            for i in range(m):
                if needle[i] != haystack[start + i]:
                    break
                if i == m - 1:
                    return start
        
        return -1




