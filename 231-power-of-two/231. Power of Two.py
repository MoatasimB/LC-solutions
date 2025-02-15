class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        def dfs(n):
            if n == 1:
                return True
            if n % 2:
                return False
            
            if dfs(n/2):
                return True
            
            return False
        
        return dfs(n)