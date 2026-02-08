class Solution:
    def dominantIndices(self, nums: List[int]) -> int:

        n = len(nums)
        averages = [0] * n

       
        s = 0
        count = 0
        for i in range(n - 1, -1, -1):
            count += 1
            s += nums[i]
            averages[i] = s / count

        ans =0 
        for i in range(n - 1):
            if nums[i] > averages[i + 1]:
                ans += 1

        return ans
            