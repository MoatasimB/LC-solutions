class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        
        nums.sort()

        l = 0
        r = len(nums) - 1
        ans = float("-inf")
        while l < r:
            ans = max(ans, nums[l] + nums[r])
            l += 1
            r -= 1
        
        return ans
