class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        ans = []

        nums.sort()
        def twoSum(l, num1):
            r = len(nums) - 1

            while l < r:
                if num1 + nums[l] + nums[r] == 0:
                    ans.append([num1, nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif num1 + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    l += 1

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] > 0:
                break
            twoSum(i + 1, nums[i])
        
        return ans
            

            
