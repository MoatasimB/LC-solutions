class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        ans = 0

        curr = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                ans = max(ans, curr)
                curr = 0
            else:
                curr +=1
        
        return max(ans, curr)