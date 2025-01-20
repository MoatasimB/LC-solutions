class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        n = len(nums)
        rightMin = [nums[-1]] * n

        
        
        for i in range(n-2, -1, -1):
            rightMin[i] = min(nums[i], rightMin[i+1])
        
        curr = nums[0]
        for i in range(1, n):
            if curr <= rightMin[i]:
                return i
            else:
                curr = max(curr, nums[i])