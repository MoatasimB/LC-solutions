class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        
        n = len(nums)
        mmin = [0] * n
        

        
        curr = nums[-1]
        mmin[-1] = curr
        for i in range(n - 2, -1, -1):
            curr = min(curr, nums[i])
            mmin[i] = curr
        
        curr = float("-inf")
        for i in range(n):
            curr = max(curr, nums[i])
            if curr - mmin[i] <= k:
                return i
        
        return -1
