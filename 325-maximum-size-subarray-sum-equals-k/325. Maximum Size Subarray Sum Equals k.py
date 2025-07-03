class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        

        pre = {}
        pre[0] = -1
        curr = 0
        ans = 0
        for i in range(len(nums)):
            curr += nums[i]

            if (curr - k) in pre:
                ans = max(ans, i - pre[curr - k])
            
            if curr not in pre:
                pre[curr] = i
        
        return ans
