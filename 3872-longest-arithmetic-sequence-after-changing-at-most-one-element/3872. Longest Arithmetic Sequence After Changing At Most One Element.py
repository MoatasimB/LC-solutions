class Solution:
    def longestArithmetic(self, nums: List[int]) -> int:

        n = len(nums)
        if n <= 2:
            return n

        # diff array
        diff = [nums[i + 1] - nums[i] for i in range(n - 1)]
        m = n - 1

        # L[i] = length of equal-diff run ending at i
        L = [1] * m
        for i in range(1, m):
            if diff[i] == diff[i - 1]:
                L[i] = L[i - 1] + 1

        # R[i] = length of equal-diff run starting at i
        R = [1] * m
        for i in range(m - 2, -1, -1):
            if diff[i] == diff[i + 1]:
                R[i] = R[i + 1] + 1

        max_run = max(L)

        # Case 1: just extend the best existing arithmetic run by one element
        ans = min(n, max_run + 2)

        # Case 2: change an interior element nums[i] and try to merge left + right
        for i in range(1, n - 1):
            total = nums[i + 1] - nums[i - 1]
            if total % 2 != 0:
                continue

            d = total // 2

            left_cnt = 0
            if i - 2 >= 0 and diff[i - 2] == d:
                left_cnt = L[i - 2]

            right_cnt = 0
            if i + 1 < m and diff[i + 1] == d:
                right_cnt = R[i + 1]

            # left_cnt diffs + 2 affected diffs + right_cnt diffs
            ans = max(ans, left_cnt + right_cnt + 3)

        return min(ans, n)
        