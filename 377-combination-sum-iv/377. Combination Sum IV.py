class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}

        def dfs(target):
            if target == 0:
                return 1
            if (target) in memo:
                return memo[(target)]
            ans = 0
            for i in range(len(nums)):
                if nums[i] <= target:
                    ans += dfs(target - nums[i])
            memo[(target)] = ans
            return ans
        x =  dfs(target)
        return x


       
