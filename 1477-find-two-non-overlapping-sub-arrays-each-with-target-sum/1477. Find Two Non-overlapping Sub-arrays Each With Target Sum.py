class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        sums = {0 : -1}
        n = len(arr)
        dp = [float("inf")] * (n + 1)
        curr = 0
        ans = float("inf")
        for i in range(n):
            curr += arr[i]
            dp[i + 1] = dp[i]
            if (curr - target) in sums:
                #this is a valid subarray
                idx = sums[curr - target]
                length = i - idx
                ans = min(ans, length + dp[idx + 1])

                dp[i + 1] = min(dp[i], length)
            sums[curr] = i
        
        return ans if ans != float("inf") else -1