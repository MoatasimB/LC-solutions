class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        def twoSum(l, r, num):            
            while l < r:
                if nums[l] + nums[r] + num == 0:
                    ans.append([nums[l], nums[r], num])

                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    l += 1
                elif nums[l] + nums[r] + num > 0:
                    r -= 1
                else:
                    l += 1
            

        i = 0
        while i < (len(nums) - 1):
            num = nums[i]

            if num > 0:
                break
            
            twoSum(i + 1, len(nums) - 1, num)

            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1
            i += 1
        
        return ans
            

