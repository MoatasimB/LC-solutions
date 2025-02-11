class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        x = len(nums)
        nums = nums + nums
        stack = []
        ans = [-1] * len(nums)
        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                idx = stack.pop()
                if ans[idx] == -1:
                    ans[idx] = nums[i]
            
            stack.append(i)
        
        # lastEl = nums[-1]

        # for num in nums:
        #     if num > lastEl:
        #         ans[-1] = num
        
        return ans[:x]