class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        n = len(nums)
        leftMax = [nums[0]] * n
        rightMin = [nums[-1]] * n

        for i in range(1, n):
            leftMax[i] = max(nums[i], leftMax[i-1])
        
        for i in range(n-2, -1, -1):
            rightMin[i] = min(nums[i], rightMin[i+1])
        
        # print(leftMax, rightMin)
        curr = nums[0]
        for i in range(1, n):
            if curr <= rightMin[i]:
                return i
            else:
                curr = max(curr, nums[i])