class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        set_nums = {n:i for i, n in enumerate(nums)}
        
        seen = set()
        
        ans = 0
        for i in range(len(nums)):
          
            if nums[i] not in seen:
                seen.add(nums[i])
                curr = 1
                start = nums[i]
                while start - 1 in set_nums:
                    seen.add(start - 1)
                    start -= 1
                    curr += 1 
                
                start = nums[i]
                while start + 1 in set_nums:
                    seen.add(start + 1)
                    start += 1
                    curr += 1
                
                ans = max(curr, ans)
        
        return ans
                
                