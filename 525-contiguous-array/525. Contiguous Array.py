class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        last = {}
        last[0] = -1

        curr = 0
        ans = 0
        for i, num in enumerate(nums):
            if num == 1:
                curr += 1
            else:
                curr -= 1
            if curr in last:
                ans = max(ans, i - last[curr])
            
            if curr not in last:
                last[curr] = i
        return ans

