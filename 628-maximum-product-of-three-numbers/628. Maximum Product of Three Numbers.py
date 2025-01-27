class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        
        nums.sort()
        if len(nums) == 3:
            curr = 1
            for num in nums:
                curr *= num
            return curr

        if nums[0] > 0:
            return nums[-1] * nums[-2] * nums[-3]
        

        return max(nums[0] * nums[1] * nums[-1], nums[-1] * nums[-2] * nums[-3])
