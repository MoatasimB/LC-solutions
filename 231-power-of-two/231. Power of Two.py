class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        def rec(n):
            if n == 1:
                return True
            
            if n % 2:
                return False
            
            return rec(n // 2)
        
        return rec(n)