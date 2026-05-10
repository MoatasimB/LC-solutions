class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        memo = {}
        def dfs(i):
            if i in memo:
                return memo[i]
            if i == n - 1:
                return 0
            
            ans = float("-inf")
            for j in range(i + 1, n):
                if abs(nums[i] - nums[j]) <= target:
                    ans = max(ans, dfs(j) + 1)
            memo[i] = ans
            return ans
        
        final = dfs(0)
        return final if final != float("-inf") else -1