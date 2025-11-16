class Solution:
    def maximizeExpressionOfThree(self, nums: List[int]) -> int:
        max1 = float("-inf")
        max2 = float("-inf")
        idx_1 = -1
        idx_2 = -1

        min_el = float("inf")
        min_idx = -1
        for i in range(len(nums)):
            if nums[i] > max1:
                max1 = nums[i]
                idx_1 = i

        for i in range(len(nums)):
            if nums[i] >= max2 and i != idx_1:
                max2 = nums[i]
                idx_2 = i

        for i in range(len(nums)):
            if nums[i] <= min_el and i!= idx_1 and i != idx_2:
                min_el = nums[i]
                min_idx = i
            



        return max1 + max2 - min_el