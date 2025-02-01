class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()

        def k_sums(nums, target, level):
            ans = []

            if not nums:
                return ans
            
            if level == 2:
                return twoSums(target, nums)
            
            for i in range(len(nums)):
                if i == 0 or nums[i-1] != nums[i]:
                    for res in k_sums(nums[i+1:], target - nums[i], level -1):
                        ans.append(([nums[i]] + res))

            return ans

        def twoSums(target, nums):
            ans = []
            l = 0
            r = len(nums) - 1
            while l <  r:
                curr = nums[l] + nums[r]
                if curr < target or (l > 0 and nums[l] == nums[l-1]):
                    l +=1
                elif curr > target or (r < len(nums)-1 and nums[r] == nums[r+1]):
                    r -= 1
                else:
                    ans.append([nums[l], nums[r]])
                    l += 1
                    r -= 1
            return ans
                    


        return k_sums(nums, target, 4)