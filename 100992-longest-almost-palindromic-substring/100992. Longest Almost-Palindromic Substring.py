class Solution:
    def almostPalindromic(self, s: str) -> int:

        n = len(s)
        # ans = 0
        # def pali(l, r):
        #     while l < r:
        #         if s[l] != s[r]:
        #             return False
        #         l += 1
        #         r -= 1
        #     return True
        # def check(l, r):
        #     while l < r:
        #         if s[l] != s[r]:
        #             return pali(l, r - 1) or pali(l + 1, r)
        #         l += 1
        #         r -= 1
        #     return True

        
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         if check(i, j):
        #             ans = max(ans, j - i + 1)

        # return ans

    # between (i, j) is pali then we can check the next two characters i - 1, j + 1, if they are not equal we can try doing i - 1, j + 2, i - 2, j + 1 to see if they are equal if they are this becomes an almost pali

    #between (i, j) is almost pali, then we can extend if i - 1 == j + 1
        ans = 0
        def check(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return r - l - 1
    
        for i in range(len(s)):
            l = i
            r = i
    
            flag = False
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    ans = max(ans, check(l - 1, r), check(l, r + 1))
                    flag = True
                    break
                else:
                    ans = max(ans, r - l + 1)
                    l -= 1
                    r += 1
            if not flag:
                if l >= 0 or r < len(s):
                    ans = max(ans, r - l)
    
            l = i
            r = i + 1
    
            flag = False
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    ans = max(ans, check(l - 1, r), check(l, r + 1))
                    flag = True
                    break
                else:
                    ans = max(ans, r - l + 1)
                    l -= 1
                    r += 1
            if not flag:
                    if l >= 0 or r < len(s):
                        ans = max(ans, r - l)
            
        return ans
    
    
    
                    