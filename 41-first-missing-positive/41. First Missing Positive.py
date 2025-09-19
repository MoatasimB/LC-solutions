class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1
        
        for i in range(n):
            idx = abs(nums[i])
            if idx < n and nums[idx] > 0:
                nums[idx] = -nums[idx] #mark as seen
            elif idx == n:
                nums[0] = -abs(nums[0])
        

        curr = 1
        while curr < n and nums[curr] < 0:
            curr += 1
        
        # for val in nums:
        #     if abs(val) == curr:
        #         curr +=1
        #         break
        
        return curr if (curr < n or (curr == n and nums[0] > 0)) else curr + 1

        [-3, -4, 5, -1]
