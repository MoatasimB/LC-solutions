class Solution:
    def findMin(self, nums: List[int]) -> int:

        l = 0
        r = len(nums) - 1
        if nums[0] <= nums[r]:
            return nums[0]
        
        while l <= r:
            mid = (l + r) // 2

            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            
            if mid + 1 < len(nums) and nums[mid + 1] < nums[mid]:
                return nums[mid + 1]
            

            if nums[l] < nums[mid]:
                l = mid + 1
            else:
                r = mid - 1