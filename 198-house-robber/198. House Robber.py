class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        def dfs(i):
            if i == 0:
                return nums[0]
            
            if i == 1:
                return max(nums[1], nums[0])

            if i in dp:
                return dp[i]
            
            dp[i] = max(nums[i] + dfs(i-2), dfs(i-1))

            return dp[i]
        
        return dfs(len(nums) - 1)

