class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        
        seen = defaultdict(int)
        count = 0 
        for i in range(len(nums)):
            if nums[i] - i in seen:
                count += seen[nums[i] - i]

            seen[nums[i] - i] += 1
  
        return ((len(nums) * (len(nums) - 1)) // 2) - count