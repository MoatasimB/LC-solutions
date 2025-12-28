class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        # if target < nums[0] or target > nums[-1]:
        #     return [-1, -1]
        

        l = 0
        r = len(nums) - 1
        ans = -1
        while l <= r:
            mid = (l + r) // 2

            if nums[mid] >= target:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        
        if nums[ans] != target:
            return [-1, -1]
        
        left = ans

        l = 0
        r = len(nums) - 1
        ans = -1
        while l <= r:
            mid = (l + r) // 2

            if nums[mid] <= target:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        
        return [left, ans]
        