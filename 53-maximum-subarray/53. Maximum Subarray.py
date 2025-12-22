class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        curr = 0
        ans = float("-inf")

        for num in nums:
            if curr < 0:
                curr = 0
            
            curr += num
            ans = max(ans, curr)
        
        return ans