class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        if n == 0:
            return False
        return (n & (-n)) == n

        def rec(n):
            if n == 1:
                return True
            
            if n % 2:
                return False
            
            return rec(n // 2)
        
        return rec(n)

        10000
        11111

        10000