class Solution:
    def longestArithmetic(self, nums: List[int]) -> int:

        n = len(nums)
        if n <= 2:
            return n

        diff = [nums[i + 1] - nums[i] for i in range(n - 1)]
        m = n - 1

        # L[i] = length of same-diff run ending at i
        L = [1] * m
        for i in range(1, m):
            if diff[i] == diff[i - 1]:
                L[i] = L[i - 1] + 1

        # R[i] = length of same-diff run starting at i
        R = [1] * m
        for i in range(m - 2, -1, -1):
            if diff[i] == diff[i + 1]:
                R[i] = R[i + 1] + 1

        max_run = max(L)

        # No internal bridge: just extend a longest arithmetic block by changing one endpoint
        ans = min(n, max_run + 2)

        # Try changing each internal element nums[k]
        for k in range(1, n - 1):
            gap = nums[k + 1] - nums[k - 1]
            if gap % 2 != 0:
                continue

            x = gap // 2

            left = 0
            if k - 2 >= 0 and diff[k - 2] == x:
                left = L[k - 2]

            right = 0
            if k + 1 <= m - 1 and diff[k + 1] == x:
                right = R[k + 1]

            ans = max(ans, left + right + 3)

        return min(ans, n)
                    
        

