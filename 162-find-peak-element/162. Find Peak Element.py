class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = len(nums) - 1
     
        while l<=r:
            mid = (l+r) // 2
            if mid == n - 1:
                if nums[mid] > nums[mid-1]:
                    return mid
                else:
                    r = mid -1
            elif mid == 0:
                if nums[mid] > nums[mid+1]:
                    return mid
                else:
                    l = mid + 1
            else:
                if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                    return mid
                elif nums[mid+1] > nums[mid]:
                    l = mid + 1
                    continue
                elif nums[mid-1] > nums[mid]:
                    r = mid - 1
        
        return 0
