class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)

        min_idx = -1
        max_idx = -1
        max_val = float("-inf")
        min_val = float("inf")

        for i in range(n):
            if nums[i] > max_val:
                max_val = nums[i]
                max_idx = i
            if nums[i] < min_val:
                min_val = nums[i]
                min_idx = i
        #all front

        rightIdx = max(min_idx, max_idx)

        #all back
        leftIdx = min(min_idx, max_idx)

        #front and back

        frontDistance = leftIdx + 1
        backDistance = n - rightIdx

        return min(rightIdx + 1, n - leftIdx, frontDistance + backDistance)
