class Solution:
    def integerBreak(self, n: int) -> int:
        memo = {}
        def dfs(num):
            if num in memo:
                return memo[num]
            if num == 1:
                return 1
            
            ans = 0 if num == n else num

            for i in range(1, num):
                ans = max(ans, dfs(i) * dfs(num - i))
            
            memo[num] = ans
        
            return ans
        
        return dfs(n)
