class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        counts = {0 : 1}
        ans = 0
        curr = 0
        for num in nums:
            curr += num

            if (curr - k) in counts:
                ans += counts[(curr - k)]
            
            if curr in counts:
                counts[curr] += 1
            else:
                counts[curr] = 1
        
        return ans
