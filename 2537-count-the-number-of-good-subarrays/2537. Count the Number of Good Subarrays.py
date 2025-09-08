class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        

        counts = defaultdict(int)
        l = 0
        ans = 0
        pairs = 0
        for r in range(len(nums)):
            pairs += counts[nums[r]]
            counts[nums[r]] += 1
            
            while pairs >= k:
                ans += len(nums) - 1 - r + 1
                counts[nums[l]] -= 1
                pairs -= counts[nums[l]]
     
                l += 1
            
        
        return ans

 