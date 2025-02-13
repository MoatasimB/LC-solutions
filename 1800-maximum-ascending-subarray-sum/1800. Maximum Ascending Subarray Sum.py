class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        
        ans = nums[0]
        curr = nums[0]
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                curr += nums[i]
                ans = max(ans, curr)
            else:
                curr = nums[i]
        
        return ans

