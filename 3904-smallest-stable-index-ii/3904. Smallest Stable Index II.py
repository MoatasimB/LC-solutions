class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        
        n = len(nums)
        mmax = [0] * n
        mmin = [0] * n
        
        curr = nums[0]
        mmax[0] = curr
        for i in range(1, n):
            curr = max(curr, nums[i])
            mmax[i] = curr
        
        curr = nums[-1]
        mmin[-1] = curr
        for i in range(n - 2, -1, -1):
            curr = min(curr, nums[i])
            mmin[i] = curr
        

        for i in range(n):
            if mmax[i] - mmin[i] <= k:
                return i
        
        return -1
