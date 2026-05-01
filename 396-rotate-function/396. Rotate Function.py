class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        

        ans = 0
        n = len(nums)

        total = sum(nums)
        for i in range(n):
            ans += i * nums[i]
        
        curr = ans
        for i in range(n - 1, -1, -1):
            remove = nums[i]
            curr = curr - ((n-1)* remove) + (total - remove)
            ans = max(ans, curr)
            # -6
            # + 4
            # + 3 
            # + 2

        return ans
