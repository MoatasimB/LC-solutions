class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        
        i = 0
        j = 0
        n = len(s)
        ans = 0
        while j < n:
            j = i
            firstVal = s[i]
            firstCount = 0
            while j < n and s[j] == firstVal:
                j += 1
                firstCount += 1
            if j == n:
                break
            secondVal = s[j]
            nextStart = j
            secondCount = 0
            while j < n and s[j] == secondVal:
                j += 1
                secondCount += 1
            ans += min(secondCount, firstCount)
            i = nextStart
        return ans
