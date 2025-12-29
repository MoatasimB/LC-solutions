class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()

        def twoSum(l, target):
            r = len(nums) - 1
            while l < r:

                if nums[l] + nums[r] == target:
                    ans.append(quad + [nums[l]] + [nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l - 1] == nums[l]:
                        l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    l += 1
        
        ans = []
        quad = []
        def kSum(l, k, target):
            if k == 2:
                return twoSum(l, target)
            
            i = 0

            for i in range(l, len(nums) - k + 1):
                if i > l and nums[i] == nums[i - 1]:
                    continue
                quad.append(nums[i])
                kSum(i + 1, k - 1, target - nums[i])
                quad.pop()

        kSum(0, 4, target)
        return ans