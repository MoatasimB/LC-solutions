class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def dfs(x, n):
            if n == 0:
                return 1
            
            ans = 0
            if n % 2 == 0:
                ans += dfs(x * x, n // 2) 
            else:
                ans += x * dfs(x * x, n // 2)
            
            return ans
        
        neg = False
        if n < 0:
            neg = True
        final = dfs(x, abs(n))
        
        return 1/final if neg else final