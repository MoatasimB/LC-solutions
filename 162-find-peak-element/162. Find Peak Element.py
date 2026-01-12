class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        l = 0
        r = len(nums) - 1
        
        while l < r:
            mid = (l + r) // 2
            
            prev = nums[mid - 1] if (mid - 1 >= 0) else float("-inf")
            n = nums[mid + 1] if (mid + 1 < len(nums)) else float("inf")
            
            if prev < nums[mid] and nums[mid] > n:
                return mid
            if nums[mid] < nums[mid + 1]:
                l = mid + 1
            else:
                r = mid
        
        
        return l