class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)

        half = s[:(n // 2)]

        half = "".join(sorted(half))
       

        if n % 2 == 1:
            return half + s[n // 2] + half[::-1]
        
        return half + half[::-1]
