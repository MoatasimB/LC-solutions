class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        l = 0
        curr = 0
        start = 0
        length = float("inf")
        for r in range(len(nums)):
            curr += nums[r]

            while curr >= target:
                length = min(length, r-l+1)
                curr -= nums[l]
                l +=1
            

        
        return length if length != float("inf") else 0


