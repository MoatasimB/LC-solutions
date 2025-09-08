class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        from sortedcontainers import SortedList

        lst = SortedList()

        ans = float("inf")
        for i in range(len(nums)):
            if i - x >= 0:
                lst.add(nums[i-x])
            
            idx = lst.bisect_left(nums[i])

            if 0 <= idx < len(lst):
                ans = min(ans, abs(nums[i] - lst[idx]))
            if 0 <= idx - 1 < len(lst):
                ans = min(ans, abs(nums[i] - lst[idx - 1]))
            
        return ans
