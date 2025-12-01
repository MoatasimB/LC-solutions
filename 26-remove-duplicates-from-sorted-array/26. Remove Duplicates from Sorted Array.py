class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        curr = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[curr - 1]:
                nums[curr], nums[i] = nums[i], nums[curr]
                curr += 1
        
        return curr