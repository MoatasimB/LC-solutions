class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        
        if k == 1:
            return 0
        
        nums.sort()

        ans = float("inf")
        n = len(nums)
        for i in range(n - k + 1):
            min_ = float("inf")
            max_ = float("-inf")
            for j in range(i, i + k):
                min_ = min(min_, nums[j])
                max_ = max(max_, nums[j])
            ans = min(ans, max_ - min_)
        

        
        return ans