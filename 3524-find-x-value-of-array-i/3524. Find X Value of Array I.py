class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        
        n = len(nums)
        dp = [[0] * k for _ in range(n)]

        ans = [0] * k
        dp[0][nums[0] % k] += 1

        for i in range(1, n):
            num = nums[i]
            rem = num % k
            dp[i][rem] += 1

            for j in range(k):
                dp[i][(j * num) % k] += dp[i - 1][j]
        
        for i in range(n):
            for j in range(k):
                ans[j] += dp[i][j]
        
        return ans
        


                

