class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        # count = 0
        # for i in range(len(nums) - 1, -1, -1):
        #     if nums[0] * k >= nums[i]:
        #         break
        #     count += 1
        

        # count2 = 0

        # for i in range(len(nums)):
        #     if nums[i] * k >= nums[-1]:
        #         break
        #     count2 += 1
        
        # return min(count, count2)


        # 12 32 89 91 134,155, 410, 493, 607, 740, 944


        ans = 0
        left = 0
        for right in range(len(nums)):
            if nums[right] > nums[left] * k:
                ans += 1
                left += 1

        return ans
        
       
        #   1 2 5
        #     i
        #     j