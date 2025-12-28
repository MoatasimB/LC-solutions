class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        n = len(nums)

        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1
        
        containsN = False

        for i in range(n):
            if abs(nums[i]) < n:
                if nums[abs(nums[i])] > 0:
                    nums[abs(nums[i])] *= -1
            elif abs(nums[i]) == n:
                containsN = True
        

        for i in range(1, n):
            if nums[i] > 0:
                return i
        
        if containsN: return n + 1

        return n
            