class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        i = 0
        start = 0
        finish = 0
        curr = 0
        while i < len(s):

            l = i
            r = i

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l)+1 > curr:
                    curr = (r-l) + 1
                    start = l
                    finish = r
                l -=1
                r +=1
            
            l = i
            r = i + 1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l)+1 > curr:
                    curr = (r-l) + 1
                    start = l
                    finish = r
                l -=1
                r +=1
            i+=1
        
        return s[start:finish+1]
