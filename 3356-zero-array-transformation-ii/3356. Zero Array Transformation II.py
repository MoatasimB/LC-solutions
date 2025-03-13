class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        
        def check(mid):
            diff = [0] * len(nums)

            for start, end, val in queries[:mid]:
                diff[start] -= val

                if end + 1 < len(nums):
                    diff[end + 1] += val
            
            
            for i in range(1, len(diff)):
                diff[i] = diff[i] + diff[i-1]
            # print(mid, diff)
            
            for i in range(len(nums)):
                if abs(diff[i]) < abs(nums[i]):
                    return False
            
            return True
        
        l = 0
        r = len(queries)
        ans = float('inf')
        while l <= r:
            mid = (l+r) // 2

            if check(mid):
                r = mid - 1
                ans = min(ans, mid)
            else:
                l = mid + 1
        
        return ans if ans != float('inf') else -1


