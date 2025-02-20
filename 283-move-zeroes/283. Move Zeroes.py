class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

   
        # r=0

        # for l in range(len(nums)):
        #     if nums[l] == 0 and l!=len(nums) - 1:
        #         while nums[r]==0 and r<len(nums) - 1:
        #             r+=1 
        #         nums[l], nums[r] = nums[r], nums[l]
        
        l = 0

        for r in range(len(nums)):
            if nums[r] != 0:
                nums[r], nums[l] = nums[l], nums[r]
                l+=1
        
            
