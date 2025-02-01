class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        
        pre = [nums[0]]

        for i in range(1, len(nums)):
            pre.append(pre[-1] + nums[i])
        print(pre)
        ans = 0
        for i in range(len(nums) - 1):
            left = pre[i]
            right = nums[i+1] + pre[-1] - pre[i+1]
            # right = pre[-1] - left
            print(left, right)
            if left >= right:
                ans +=1
        
        return ans
