class Solution:
    def reverse(self, x: int) -> int:
        
        lst = []
        negative = x < 0
        x = abs(x)
        
        while x:
            digit = x % 10
            x = x // 10
            lst.append(digit)
        
        power = 1
        ans = 0
        for i in range(len(lst)-1,-1,-1):
            if ans + (lst[i] * power) > 2**31:
                return 0
            ans += lst[i] * power
            power *=10
        
        
        if negative:
            return -1 * ans
        
        return ans
