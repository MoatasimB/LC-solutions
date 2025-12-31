class Solution:
    def shortestPalindrome(self, s: str) -> str:
        

        def makeLPS(s):

            newString = s + "#" + s[::-1]

            lps = [0] * len(newString)

            _len = 0
            i = 1

            while i < len(newString):
                if newString[i] == newString[_len]:
                    _len += 1
                    lps[i] = _len
                    i += 1
                else:
                    if _len != 0:
                        _len = lps[_len - 1]
                    else:
                        i += 1
            
            return lps
        
        lps = makeLPS(s)

        suffix = lps[-1]
        
        rev_string = s[suffix:]
        rev_string = rev_string[::-1]
        return rev_string + s

