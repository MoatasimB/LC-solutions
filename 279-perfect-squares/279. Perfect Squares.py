class Solution:
    def numSquares(self, n: int) -> int:
        
#         [1 4, 9, 16 ....n]
        
        
#         [1,2,3,4....sqrtN]
        # [1,2,3...84]

        squares = [i**2 for i in range(1, int(math.sqrt(n)) + 1)]
        # memo = {}
    
        # def dfs(target):
        #     if (target) in memo:
        #         return memo[(target)]
        #     if target == 0:
        #         return 0
        #     ans = float("inf")
        #     for num in squares:
        #         if num <= target:
        #             ans = min(ans, 1 + dfs(target - num))
            
        #     memo[(target)] = ans
        #     return ans
        
        # return dfs(n)
    
    
  
        dp = [float("inf")] * (n + 1)
        dp[0] = 0

        for target in range(1, n+1):

            for num in squares:
                if num <= target:
                    dp[target] = min(dp[target], 1 + dp[target - num])
        
        return dp[n]

                
