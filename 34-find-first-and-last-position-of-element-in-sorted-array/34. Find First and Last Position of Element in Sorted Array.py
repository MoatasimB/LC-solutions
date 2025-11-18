class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        l = 0
        r = len(nums) - 1
        flag = False
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                flag = True
                break
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        if not flag:
            return [-1,-1]
        def firstO(target):
            l = 0
            r = len(nums) - 1
            ans = -1
            while l <= r:
                mid = (l + r) // 2

                if nums[mid] < target:
                    ans = mid
                    l = mid + 1
                else:
                    r = mid - 1
            return ans
        
        def lastO(target):
            l = 0
            r = len(nums) - 1
            ans = 0
            while l <= r:
                mid = (l + r) // 2

                if nums[mid] <= target:
                    ans = mid
                    l = mid + 1
                else:
                    r = mid - 1
            return ans
        
        f = firstO(target)
        l = lastO(target)
        # if f == 0:
        #     return [f, l]
        if f + 1 < len(nums) and nums[f + 1] == target:
            return [f + 1,l]
        
        # return [f, l]
        # if f == -1 or l == -1:
        #     return [-1,-1]
        # if f + 1 < len(nums) and nums[f + 1] == target:
        #     return [f + 1,l]
        # return [-1,-1]