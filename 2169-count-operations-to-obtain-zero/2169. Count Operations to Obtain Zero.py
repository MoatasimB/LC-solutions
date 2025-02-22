class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        
        def rec(n1, n2):
            if n1 == 0 or n2 == 0:
                return 0
            if n1 == n2:
                return 1
            ans = 0
            if n1 > n2:
                ans = 1 + rec(n1-n2, n2)
            else:
                ans = 1 + rec(n1, n2 - n1)

            return ans
        
        return rec(num1, num2)
        
        