class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        def makeLPS(needle):
            m = len(needle)
            lps = [0] * m
            
            i = 1
            _len = 0 
            while i < m:

                if needle[i] == needle[_len]:
                    _len += 1
                    lps[i] = _len
                    i += 1
                else:
                    if _len != 0:
                        _len = lps[_len - 1]
                    else:
                        lps[i] = 0
                        i += 1
            return lps
        

        lps = makeLPS(needle)

        j = 0
        i = 0

        while i < len(haystack):

            if needle[j] == haystack[i]:
                j += 1
                i += 1

                if j == len(needle):
                    return i - len(needle)
            else:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        
        return -1
