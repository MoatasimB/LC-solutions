class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums = set(nums)
        ans = 0
        for num in nums:
            if num - 1 in nums:
                continue
            
            curr = 1
            start = num
            while start + 1 in nums:
                curr += 1
                start += 1
            
            ans = max(ans,  curr)
        
        return ans