class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        
        n = len(nums)
        mmax = [float("-inf")] * n
        mmin = [float("inf")] * n
        mmax[0] = nums[0]
        mmin[-1] = nums[-1]
        for i in range(1, n):
            mmax[i] = max(mmax[i - 1], nums[i])
        
        for i in range(n - 2, -1, -1):
            mmin[i] = min(mmin[i + 1], nums[i])
        

        for i in range(n):
            left = mmax[i]
            right = mmin[i]
            if left - right <= k:
                return i
        
        return -1