class Solution:
    def rob(self, nums: List[int]) -> int:

        dp = [0] * len(nums)

        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        # dp[0] = nums[0]
        # dp[1] = max(nums[0], nums[1])
        two = nums[0]
        one = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            curr = max(nums[i] + two, one)
            two = one
            one = curr 
            # dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        
        return one

