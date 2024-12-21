class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        

        l = 0
        r = 1
        while r<len(nums):
            while r<len(nums) and nums[r] == nums[l]:
                r +=1
            if r >= len(nums):
                return l+1
            
            nums[l+1], nums[r] = nums[r], nums[l+1]
            l+=1
            r+=1
        return l+1

