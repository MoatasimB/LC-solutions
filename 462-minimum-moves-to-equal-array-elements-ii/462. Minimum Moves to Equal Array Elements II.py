class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        s = sum(nums)
        n = len(nums)
        mid_low = s // n
        mid_high = mid_low + 1
        mid_num_low = nums[n // 2]
        mid_num_high = nums[n // 2 + 1] if (n // 2 + 1) < n else None
        c1 = 0
        c2 = 0
        c3 = 0
        c4 = 0
        print(mid_low, mid_high)
        for i in range(n):
            c1 += abs(nums[i] - mid_low)
            c2 += abs(nums[i] - mid_high)
            c3 += abs(nums[i] - mid_num_low)
            if mid_num_high:
                c4 += abs(nums[i] - mid_num_high)
        print(c1, c2, c3, c4)
        ans = min(c1, c2, c3)
        if mid_num_high:
            ans = min(ans, c4)
        
        return ans
