class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        
        n = len(nums)
        dp = [[0] * k for _ in range(n)]
        dp[0][nums[0] % k] += 1

        ans = [0] * k

        for i in range(1, n):
            num = nums[i]
            rem = num % k
            dp[i][rem] += 1

            for j in range(k):
                dp[i][(j * nums[i]) % k] += dp[i - 1][j]
        for i in range(n):
            for j in range(k):
                ans[j] += dp[i][j]
        
        return ans
        


                

#dp[i][r] = #of subarrays ending at idx i that have remainder r