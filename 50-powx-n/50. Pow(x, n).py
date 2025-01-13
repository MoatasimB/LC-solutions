class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def p(num, exp):
            
            if exp == 1:
                return num
            if exp == 0:
                return 1
            new_num = num * num
            if exp % 2:
                return num * p(new_num, (exp - 1) // 2)
            else:
                return p(new_num, exp // 2)
        
        num = p(x, abs(n))

        return num if n > 0 else 1 / num