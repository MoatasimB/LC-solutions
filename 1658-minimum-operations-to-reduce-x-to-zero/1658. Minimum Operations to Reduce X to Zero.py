class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
   
        n = len(nums)

        l = 0
        total = sum(nums)
        # if total == x:
        #     return n
        curr = 0
        ans = float("inf")
        for r in range(n):
            curr += nums[r]
            while l <= r and total - curr < x:
                curr -= nums[l]
                l += 1
            
            if total - curr == x:
                left = l
                right = n - r - 1
                ans = min(ans, left + right)
        return ans if ans != float("inf") else -1



