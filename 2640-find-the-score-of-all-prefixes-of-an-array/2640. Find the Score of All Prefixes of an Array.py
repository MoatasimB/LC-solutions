class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        
        ans = [nums[0]*2]
        maxSoFar = nums[0]
        
        for i in range(1, len(nums)):
            maxSoFar = max(maxSoFar, nums[i])
            ans.append(ans[-1] + nums[i] + maxSoFar)
        
        return ans

