class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        
        n = len(nums)
        memo = {}
        def dfs(i, p):
            if (i, p) in memo:
                return memo[(i, p)]
            if p == 0:
                return 0
            if i == n:
                return float("inf")
            ans = float("inf")


            for j in range(i, n):
                ans = min(ans, nums[i] + dfs(j + 1, p - 1))
            
            memo[(i, p)] = ans
            return ans
        
        return dfs(0, 3)

        # dfs(0, 3)


        # 5 + dfs(1, 2)

        #     4 + dfs()