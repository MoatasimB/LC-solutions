class Solution:
    def smallestBalancedIndex(self, nums: list[int]) -> int:

        # leftSum = [nums[0]]
        n = len(nums)
        total = sum(nums)
        limit = total + 1
        ans = -1
        right = 1
        # for i in range(1, len(nums)):
        #     leftSum.append(leftSum[-1] + nums[i])
        for i in range(n - 1, -1, -1):
            total -= nums[i]

            if total == right:
                ans = i

            if right <= limit:
                right *= nums[i]
                if right > limit:
                    break
        return ans

       
        # right = 1
        # for i in range(n):
        #     right = min(L, right *nums[i])
        
        # left = 0
        # for i in range(n):
        #     right = right // nums[i] if right < L else L
        #     if left == right:
        #         return i
        #     left += nums[i]
            
        # return -1
            