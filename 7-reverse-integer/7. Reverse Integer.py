class Solution:
    def reverse(self, x: int) -> int:
        
        sign = -1 if x < 0 else 1

        ans = 0
        x = abs(x)
        while x:
            digit = x % 10

            ans = ans * 10 + digit

            if ans > (2**31) - 1:
                return 0
            
            x = x // 10
        
        return sign * ans