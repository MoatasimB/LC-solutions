class Solution:
    def rotatedDigits(self, n: int) -> int:
        
        ans = 0
        for i in range(1, n + 1):
            str_int = str(i)
            if "3" in str_int or "4" in str_int or "7" in str_int:
                continue
            if "2" in str_int or "5" in str_int or "6" in str_int or "9" in str_int:
                ans += 1
        
        return ans