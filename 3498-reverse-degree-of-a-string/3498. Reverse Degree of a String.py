class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0
        for idx in range(len(s)):
            ch = s[idx]
            i = idx + 1
            val = 26 - (ord(ch) - ord("a"))
            ans += val * i
        
        return ans