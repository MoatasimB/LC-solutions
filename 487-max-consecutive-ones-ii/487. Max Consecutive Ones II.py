class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        
        n = len(nums)

        l = 0
        zero_idx = None
        ans = 0
        for r in range(n):

            if nums[r] == 0:
                if zero_idx != None:
                    l = zero_idx + 1 if zero_idx else 1
                zero_idx = r
            ans = max(ans, r - l + 1)
        
        return ans

        # [0, 0]
        # l
        #     r
        #  z