class Solution:
    def minOperations(self, nums: list[int]) -> int:


        n = len(nums)
    
        ans = 0
    
        curr = 0
    
        for i in range(1, n):
            if nums[i - 1] > nums[i]:
                diff = abs(nums[i] - nums[i - 1])
                ans += diff
                curr += diff
    
        return ans