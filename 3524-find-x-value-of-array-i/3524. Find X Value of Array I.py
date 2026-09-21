class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        
        n = len(nums)
        dp = [[0] * k for _ in range(n)]

        ans = [0] * k

        for i in range(n - 1):
            num = nums[i]
            rem = num % k
            dp[i][rem] += 1

            for j in range(k):
                dp[i + 1][(j * nums[i + 1]) % k] += dp[i][j]
        dp[n - 1][nums[n-1] % k] += 1
        for i in range(n):
            for j in range(k):
                ans[j] += dp[i][j]
        
        return ans
        


                

#dp[i][r] = #of subarrays ending at idx i that have remainder r