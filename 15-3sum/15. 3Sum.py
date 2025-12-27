class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        ans = []
        def twoSum(l, r, curr):
            
            while l < r:
                if nums[l] + nums[r] + curr == 0:
                    ans.append([curr, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif nums[l] + nums[r] + curr > 0:
                    r -= 1
                else:
                    l += 1

        

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            
            if i == 0 or nums[i] != nums[i - 1]:
                twoSum(i + 1, len(nums) - 1, nums[i])
        
        return ans
