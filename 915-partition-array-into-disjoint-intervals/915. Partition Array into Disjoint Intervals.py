class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        
        largestWeSeen = nums[0]
        largest = nums[0]
        ans = 0
        for i in range(1, len(nums)):
            if nums[i] < largest:
                ans = i
                largest = largestWeSeen
            else:
                largestWeSeen = max(largestWeSeen, nums[i])

        return ans + 1
        
        
        
        