class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        for i in range(len(haystack)):
            j = i
            n = 0
            while j < len(haystack) and n < len(needle) and haystack[j] == needle[n]:
                j +=1
                n +=1
            
            if n == len(needle):
                return i
        
        return -1
