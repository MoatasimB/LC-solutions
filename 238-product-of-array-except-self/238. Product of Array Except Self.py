class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        front = [1] * n
        back = [1] * n

        prev = 1
        for i in range(len(nums)):
            front[i] = prev * nums[i]
            prev *= nums[i]

        prev = 1
        for i in range(len(nums) - 1, -1, -1):
            back[i] = prev * nums[i]
            prev *= nums[i]
        
        ans = [1] * n

        for i in range(1, len(nums) - 1):
            ans[i] = front[i-1] * back[i+1]
        print(front)
        print(back)
        ans[0] = back[1]
        ans[n-1] = front[n-2]
        return ans

