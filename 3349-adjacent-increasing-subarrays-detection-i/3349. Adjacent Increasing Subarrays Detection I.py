class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        
        prev = 0
        curr = 1
        ans = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                curr += 1
            else:
                prev = curr
                curr = 1
            
            ans = max(ans, min(prev, curr))
            ans = max(ans,curr // 2 )
        
        return ans >= k


            