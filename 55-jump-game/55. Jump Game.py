class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        goal = len(nums) - 1

        i = len(nums) - 2

        while i >= 0:
            if nums[i] + i >= goal:
                print(nums[i], i, goal)
                goal = i
            i -= 1
        
        return goal <=0

