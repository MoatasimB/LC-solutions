class Solution:
    def minMoves(self, nums: List[int]) -> int:
        
        max_n = max(nums)

        return sum(abs(nums[i] - max_n) for i in range(len(nums)))