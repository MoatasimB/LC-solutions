class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        dp = {}
        def dfs(left, right):
            if left > right:
                return 0
            if (left, right) in dp:
                return dp[(left, right)]
            ans = 0
            for j in range(left, right + 1):

                burst = nums[left - 1] * nums[j] * nums[right + 1] + dfs(j + 1, right) + dfs(left, j - 1)
                ans = max(ans, burst)
            
            dp[(left, right)] = ans
            return ans

        return dfs(1, len(nums) - 2)

                    