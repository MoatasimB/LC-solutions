class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        total = sum(nums)
        pos = 0
        for num in nums:
            if num > 0:
                pos += 1
        if pos == 0:
            return max(nums)

        curr = 0
        ans = max(total, max(nums))

        for num in nums:
            if curr < 0:
                curr = 0
            curr += num
            ans = max(ans, curr, total - curr)
        

        curr = 0
        for num in nums:
            if curr > 0:
                curr = 0
            
            curr += num
            ans = max(ans, curr, total - curr)
        
        return ans
