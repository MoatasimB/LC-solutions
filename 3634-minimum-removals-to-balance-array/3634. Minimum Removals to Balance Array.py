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


        n = len(nums)
        i = 0
        j = 0
        ans = float("inf")
        while j < n:
            while j < n and nums[i] * k >= nums[j]:
                j += 1
            ans = min(ans, n - (j - i))
            i += 1
            j = max(j, i)
        
        return ans
        
       
        #   1 2 5
        #     i
        #     j