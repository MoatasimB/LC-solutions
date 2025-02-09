class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        
        ans = 1
        increasing = 0
        decreasing = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                ans = max(i - increasing + 1, ans)
                decreasing = i
            elif nums[i] < nums[i-1]:
                ans = max(i - decreasing + 1, ans)
                increasing = i
            else:
                increasing = i
                decreasing = i
        
        return ans
