class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        n = len(nums)

        l = 0
        r = n - 1

        while l <= r:
            mid = (l + r) // 2
            prev = nums[mid - 1] if mid - 1 >= 0 else float("-inf")
            curr = nums[mid]

            if curr > prev:
                l = mid + 1
            else:
                r = mid - 1
            
        
        return r
