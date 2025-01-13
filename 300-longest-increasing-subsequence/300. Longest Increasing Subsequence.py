class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        # dp = {}
        # dp[0] = 1

        # def dfs(i):

        #     if i == 0:
        #         return 1
        #     if i in dp:
        #         return dp[i]
        #     curr = float("-inf")
        #     for j in range(i-1, -1, -1):
        #         if nums[j] < nums[i]:
        #             curr = max(curr, 1 + dfs(j))
            
        #     dp[i] = curr if curr != float('-inf') else 1
            
        #     return dp[i]
        
        # for i in range(len(nums)-1, -1,-1):
        #     dfs(i)

        # return max(dp.values())

        dp = {}
        for i in range(len(nums)):
            curr = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    curr = max(curr, 1 + dp[j])

            dp[i] = curr
            
        return max(dp.values())