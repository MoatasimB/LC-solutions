class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        l = 0
        r = len(nums) -1 
        leftmost = -1

        while l<=r:
            mid = (l+r) // 2

            if nums[mid] >= target:
                if nums[mid] == target:
                    leftmost = mid
                r = mid - 1
            else:
                l = mid + 1
        
        
        l = 0
        r = len(nums) -1 
        rightmost = -1

        while l<=r:
            mid = (l+r) // 2

            if nums[mid] <= target:
                if nums[mid] == target:
                    rightmost = mid
                l = mid + 1
            else:
                r = mid - 1
        # rightmost = leftmost
        # if leftmost != -1:
        #     for i in range(leftmost, len(nums)):
        #         if nums[i] != target:
        #             break
        #         rightmost = i
        
        return [leftmost, rightmost]
