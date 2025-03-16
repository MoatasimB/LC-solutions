class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def check(mid):
            dp  = {}
            def dfs(i):
                if i >= len(nums):
                    return 0
                if (i) in dp:
                    return dp[(i)]
                take = float('-inf')
                if nums[i] <= mid:
                    take = 1 + dfs(i+2)
                skip = dfs(i+1)

                ans = max(take, skip)
                dp[(i)] = ans
                return ans
            return dfs(0) >= k
        
        l = min(nums)
        r = max(nums)
        final = float("inf")
        while l<=r:
            mid = (l+r) // 2

            if check(mid):
                r = mid - 1
                final = min(final, mid)
            else:
                l = mid + 1
        
        return final