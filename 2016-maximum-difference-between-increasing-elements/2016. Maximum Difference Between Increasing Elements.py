class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        
        ans = -1

        currMin = float("inf")
        

        for i in range(len(nums)):
            if nums[i] <= currMin:
                currMin = nums[i]
            else:
                ans = max(ans, nums[i] - currMin)
        
        return ans
