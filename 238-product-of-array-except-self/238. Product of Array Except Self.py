class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        front = [1] * n
        back = [1] * n

        for i in range(1, len(nums)):
            front[i] = front[i-1] * nums[i-1]

        back[n-1] = 1
        for i in range(len(nums) - 2, -1, -1):
            back[i] = back[i+1] * nums[i+1]
        
        ans = [1] * n

        for i in range(len(nums)):
            ans[i] = front[i] * back[i]

        # ans[0] = back[1]
        # ans[n-1] = front[n-2]
        return ans

