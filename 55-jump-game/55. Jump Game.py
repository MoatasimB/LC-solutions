class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        
        goal = len(nums) - 1

        i = len(nums) - 2

        while i >=0:

            if nums[i] + i >= goal:
                goal = i
            
            i -=1
        
        return goal == 0
