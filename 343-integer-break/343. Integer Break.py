class Solution:
    def integerBreak(self, n: int) -> int:
        #goal try to maximize the product
        #min product is break it into n components of size 1
        #if they are equal size of s and k components product is s^k
        #if we go through the factors from 1...n (not 1 or n) and break it into
        #k size components and then we can just take the maximum of all


        # 1 1 1 1 1 1 1 1 1 1 1 1  
   
        memo = {}
        def dfs(n, k):
            if (n, k) in memo:
                return memo[(n, k)]
            
            if k == 1:
                return n
            ans = 0
            for i in range(1, n):
                ans = max(i * dfs(n - i, k - 1), ans)
            
            memo[(n,k)] = ans
            return ans
        final = 0
        if n == 2:
            return 1
        for k in range(2, n):
            final = max(final, dfs(n, k))

        return final

