class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        
        prefixGCD = []
        n = len(nums)
        mx = 0
        for i in range(n):
            num = nums[i]
            mx = max(mx, num)
            prefixGCD.append(math.gcd(num, mx))
        
        prefixGCD.sort()
        ans = 0
        for i in range(n // 2):
            first = prefixGCD[i]
            second = prefixGCD[n - i - 1]
            ans += math.gcd(first, second)
        
        return ans
