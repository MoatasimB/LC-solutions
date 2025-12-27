class Solution:
    def longestPalindrome(self, s: str) -> str:

        n = len(s)
        currMax = 0
        currStartIdx = -1
        for i in range(n):
            l = i
            r = i

            while l  >= 0 and r < n and s[l] == s[r]:
                if (r - l + 1) > currMax:
                    currMax = (r - l + 1)
                    currStartIdx = l
                l -= 1
                r += 1

            l = i
            r = i + 1

            while l  >= 0 and r < n and s[l] == s[r]:
                if (r - l + 1) > currMax:
                    currMax = (r - l + 1)
                    currStartIdx = l
                l -= 1
                r += 1
        

        return s[currStartIdx : currStartIdx + currMax]