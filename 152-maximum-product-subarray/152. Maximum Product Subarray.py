class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)


        maxLeft = float('-inf')
        curr = 1
        for i in range(len(nums)):
            if nums[i] == 0:
                curr = 1
                continue
            curr = curr * nums[i]
            maxLeft = max(maxLeft, curr)
     
        maxRight = float('-inf')
        curr = 1
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == 0:
                curr = 1
                continue
            curr = curr * nums[i]
            maxRight = max(maxRight, curr)
        
        ans = max(maxLeft, maxRight, max(nums))
        return ans
        # [2     6   -12   -24]
        # [-48  -24   -8     4]

        # [-2 0 0]
        # [0 0 -1]
