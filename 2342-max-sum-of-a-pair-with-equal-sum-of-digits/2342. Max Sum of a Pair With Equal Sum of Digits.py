class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        
        def digitS(x):
            ans =0 
            while x:
                ans += x % 10
                x = x // 10
            return ans
        
        seen = {}
        ans = -1
        for i in range(len(nums)):
            x = digitS(nums[i])
            if x in seen:
                ans = max(ans, nums[i] + seen[x])
                if seen[x] > nums[i]:
                    continue
            seen[x] = nums[i]
        
        return ans
