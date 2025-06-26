class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        l = -1
        r = len(nums)

        i = 0

        while i < r:

            if nums[i] == 0:
                nums[i], nums[l+1] = nums[l+1], nums[i]
                l +=1
                i+=1
            elif nums[i] == 2:
                nums[i], nums[r-1] = nums[r-1], nums[i]
                r -= 1
            else:
                i += 1
        

