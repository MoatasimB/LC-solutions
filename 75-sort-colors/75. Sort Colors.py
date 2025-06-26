class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        left_border = -1
        right_border = len(nums)
        i = 0

        while i < right_border:
            if nums[i] == 0:
                nums[i], nums[left_border + 1] = nums[left_border + 1], nums[i]
                left_border += 1
                i+=1
            elif nums[i] == 2:
                nums[i], nums[right_border - 1] = nums[right_border - 1], nums[i]
                right_border -= 1
            else:
                i +=1
            
        
# # 2 0 1
#   i
# # |1 0| 2
#      i

# # 0|1|2