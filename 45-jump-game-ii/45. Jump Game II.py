class Solution:
    def jump(self, nums: List[int]) -> int:
        
        currEnd = 0
        currFarthest = 0
        ans = 0
        for i in range(len(nums) - 1):
            currFarthest = max(currFarthest, i + nums[i])

            if i == currEnd:
                ans += 1
                currEnd = currFarthest

        return ans