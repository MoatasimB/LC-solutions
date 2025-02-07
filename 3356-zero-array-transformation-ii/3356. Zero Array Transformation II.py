class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        if sum(nums) == 0:
            return 0
        def check(mid):
            diff = [0] * len(nums)
            for i in range(mid):
                start, end, val = queries[i]
                diff[start] -= val
                if end + 1 < len(nums):
                    diff[end + 1] += val
            for i in range(1, len(diff)):
                diff[i] += diff[i-1]
            for i in range(len(nums)):
                if nums[i] > abs(diff[i]):
                    return False
            return True
        
        l = 0
        r = len(queries)
        ans = float('inf')
        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                ans = min(ans, mid)
                r = mid - 1
            else:
                l = mid + 1
        
        return -1 if ans == float('inf') else ans

        for z, (start, end, val) in enumerate(queries):
            diff = [0] * len(nums)
            diff[start] -= val
            if end + 1 < len(nums):
                diff[end + 1] += val
        
            for i in range(1, len(diff)):
                diff[i] += diff[i-1]
            count = 0
            for i in range(len(nums)):
                nums[i] += diff[i]
                if nums[i] <= 0:
                    nums[i] = 0
                    count +=1
            if count == len(nums):
                return z + 1
        
        return -1

