class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        
        diff = [0] * len(nums)

        for i in range(len(queries)):
            start = queries[i][0]
            end = queries[i][1] + 1

            diff[start] -= 1
            if end <= len(nums) - 1:
                diff[end] +=1
        
        for i in range(1, len(diff)):
            diff[i] = diff[i] + diff[i-1]
        
        print(diff)
        for i in range(len(nums)):
            nums[i] = nums[i] + diff[i]

            if nums[i] < 0:
                nums[i] = 0
        
        return sum(nums) == 0