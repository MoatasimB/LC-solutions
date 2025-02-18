class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        nums = [0 if num % 2 == 0 else 1 for num in nums]

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return False
        
        return True