class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        quad = []
        ans = []
        def twoSum(l):
            r = len(nums) - 1
            
            while l < r:
                if quad[0] + quad[1] + nums[l] + nums[r] == target:
                    ans.append([quad[0], quad[1], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif quad[0] + quad[1] + nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1





        def kSum(k,l):
            if k == 2:
                twoSum(l)
                return
            
            i = l
            while i < len(nums):
                quad.append(nums[i])
                kSum(k - 1, i + 1)
                quad.pop()
                
                i += 1
                while i < len(nums) and nums[i] == nums[i - 1]:
                    i += 1
            

            # for i in range(l, len(nums)):
            #     if i == 0 or nums[i] != nums[i - 1]:
            #         quad.append(nums[i])
            #         kSum(k - 1, i + 1)
            #         quad.pop()

        kSum(4, 0)
        return ans