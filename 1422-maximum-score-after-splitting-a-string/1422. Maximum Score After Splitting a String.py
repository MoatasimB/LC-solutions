class Solution:
    def maxScore(self, s: str) -> int:
        
        nums = [int(num) for num in s]
        n = len(nums)
        for i in range(1, n):
            nums[i] += nums[i-1]
        
        ans = 0
        # print(nums)
        zeros = 0
        for i in range(n-1):
            if s[i] == '0':
                zeros += 1
            ones = nums[-1] - nums[i]
            # print(zeros, ones)
            ans = max(ans, ones + zeros)
        
        return ans

